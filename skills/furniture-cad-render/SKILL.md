---
name: furniture-cad-render
description: Turns furniture CAD drawings (front view, side view, dimension-annotated page, and any component/part drawings from a CAD PDF) into photorealistic preview images an interior designer can show a client before the piece is built. Use this whenever the user uploads furniture CAD, technical drawings, or 零件/part diagrams and asks to see what a piece will look like, wants a realistic render, a sample/demo image, an effect image (效果图), or a client-presentation preview — even if they don't use the word "render" explicitly. Also use when the user wants to check whether a generated furniture image actually matches the original CAD structure and dimensions.
---

# Furniture CAD → Realistic Preview

## What this does and why it's built this way

An interior designer uploads CAD views of a furniture piece. They don't want
to explain CAD conventions to you — they just want a photo-quality image that
looks like the real product, accurate to the actual structure and dimensions,
so they can show it to a client before anything is built. Because a wrong
render (missing drawer, wrong proportions) actively damages their credibility
with the client, correctness matters more than speed here — that's why this
skill checks its own output against the source CAD and retries before
delivering, rather than generating once and hoping.

The bundled scripts in `scripts/` implement the full pipeline with the Qwen
model family (Qwen-VL for reading the CAD, Qwen-Image for generating,
Qwen-Image-Edit for targeted fixes). Use `scripts/pipeline.py` as the entry
point — it runs the whole flow end to end. Read the other scripts if you need
to run a single step manually or debug where something went wrong.

**Deployment**: this Skill is built for Capafy's Run Online / Subscription
mode — see `config/credentials.md` for exactly which credential Capafy needs
to host and inject at runtime. Subscribers only ever provide CAD
images/PDFs and, optionally, material notes; they never need their own API
key or DashScope account.

**Setup**: these scripts need `DASHSCOPE_API_KEY` in the environment and
`pip install -r scripts/requirements.txt`. If you're running in an
environment without network access to Alibaba Cloud Model Studio, tell the
user rather than fabricating a result.

## Step 1 — Validate the input before doing anything else

A furniture render is only as good as the CAD it's based on. Before
generating anything, confirm the upload actually contains:

- A front view
- A side view
- A page with dimension annotations
- (Optional but useful) any component/part (零件) drawings extracted from the
  CAD PDF — these show individual pieces and help reconstruct the assembly

`scripts/pipeline.py` does this automatically via a vision-model check (not a
filename guess, since designers name files inconsistently).

**If something's missing or illegible**: tell the user plainly what's missing
and why it matters (e.g. "no dimension page — I can't guarantee the
proportions in the render will be accurate without one"), then ask if they
want to proceed anyway. If they say yes, continue — but the output must
clearly flag which parts are assumptions, not facts pulled from their CAD.
Never silently guess a dimension and present it as if it came from the
drawing.

Material/color/finish notes are always optional — see Step 3 below for how
that question is asked.

## Step 2 — Understand the structure

Run `scripts/vision_extract.py` (or `pipeline.py`, which calls it) on the
full image set. This produces a JSON structure — piece type, overall
dimensions, component list, material notes if visible — that becomes the
single source of truth for everything downstream. The reason this is a
separate step from generation: if the image generator works straight from
raw CAD images, it tends to hallucinate details it can't parse from a
technical drawing. Extracting structure first, in plain language and
numbers, gives the image generator something it can actually follow.

## Step 3 — Ask how many material/color versions

Before generating, ask the designer: how many material/color versions do
they want previewed (e.g. "walnut with matte black legs" vs "white oak with
brass legs" as two separate render sets), and what's the material for each?

This is one question, not a form — let them skip it entirely if they don't
care. If they skip it, generate exactly one version: use whatever material
`vision_extract` already found on the CAD, or if it found nothing, a
reasonable default for that furniture type — and label that default clearly
in the final delivery as an assumption, not a fact from their drawing.
`pipeline.py`'s `material_versions` argument takes a list for this — pass
`None`/empty to get the single default-version behavior.

Keep the number of versions reasonable (a handful, not dozens) and say why
if a designer asks for an unusually large batch — each version re-runs the
full generate-and-check loop below, so cost and time scale with it.

## Step 4 — Generate

Run `scripts/generate_image.py` against the extracted structure — but not
identically for every angle. Generate the **first angle** (the "hero," e.g.
front 3/4 view) from text via `generate_render`. Generate **every other
angle** (side view, etc.) via `generate_render_from_reference`, passing in
the hero's image as a reference, rather than generating each angle
independently from text.

The reason: two independent text-to-image calls for "front view" and "side
view" of the same piece are two separate guesses. The structure JSON pins
down dimensions and component counts, but not every visual detail — leg
style, hardware finish, exact material tone — so two independent
generations can quietly diverge on those details even though both pass
their own consistency check against the CAD. Referencing the hero's actual
pixels for every subsequent angle keeps them visually consistent with each
other, not just individually consistent with the structure. `pipeline.py`
handles this ordering automatically.

Default to 2–3 angles (front 3/4 view + side view) unless the designer asks
for something else. Output resolution is 2048×2048 — presentation quality,
not a thumbnail.

## Step 5 — Check, and retry only if it actually matters

Run `scripts/consistency_check.py` to compare each render against the
original structure. Not every mismatch deserves a retry:

- **Retry (hard fail)**: dimensions/proportions off by more than roughly
  10%, a component missing or an extra one added, wrong overall silhouette.
  These are the things a client would actually notice as "that's not what I
  designed."
- **Ship as-is (soft)**: lighting, background, texture rendering, minor
  stylistic choices. Retrying over these wastes calls and time without
  improving what the designer actually cares about.

When a retry is needed, use `scripts/edit_image.py` — it fixes only the
flagged issue on the existing image via Qwen-Image-Edit, rather than
regenerating from scratch. This matters: a full regenerate can "fix" one
problem while introducing a new one in a part that was already correct. An
edit preserves everything that already matched.

Cap retries at 3 attempts per angle. `pipeline.py` enforces this.

**If `scripts/consistency_check.py` or `edit_image.py` genuinely cannot
run** — no Python/API access in this execution environment, only a native
one-shot image tool available — do not silently skip this step and hand
back an unchecked first draft as if it were verified. This environment gap
isn't one-size-fits-all — handle whichever tier you actually have:

- **No vision-comparison capability at all**: do the best qualitative
  comparison you can with whatever vision capability you *do* have (does the
  render look like it has the right component count and rough proportions,
  per the Step 2 structure?), then **say so explicitly in the delivery** —
  e.g. "I couldn't run the automated dimension/consistency check in this
  environment; please verify proportions against the CAD before sending this
  to a client."

- **No targeted-edit / reference-conditioning capability at all** (only a
  one-shot text-to-image generator, so Step 4's hero-then-reference approach
  isn't possible either): angles will be generated independently and may
  drift from each other on details the structure JSON doesn't pin down
  (leg style, hardware, exact tone). Visually compare the angles against
  each other before delivering, and if they look inconsistent, say so
  plainly rather than presenting them as one verified set.

- **Qualitative check works and finds a real hard-fail issue, but there's no
  targeted-edit tool** (only a one-shot generator, no `edit_image.py`
  equivalent): a full regenerate is a valid fallback, but it's riskier than a
  targeted edit — it can silently change a part that was already correct
  while fixing the flagged one. So treat it more conservatively than the
  normal loop: cap it at 1–2 attempts (not 3), re-run the qualitative check
  on the new version before deciding it's good, and when you deliver, say
  plainly that this was a full regenerate rather than a targeted fix — ask
  the designer to double-check the *other* parts of the render too, not just
  the one that was flagged.

A designer acting on an unverified or riskily-patched render while believing
it was cleanly verified is worse than one who knows exactly what shortcut
was taken and what to double-check.

## Step 6 — Deliver

- Group the delivery by version if there's more than one.
- For each render that converged (passed the consistency check): present it
  plainly, noting the material used and any other assumptions.
- For any render that still doesn't fully match after 3 attempts: still
  deliver the closest result — never leave the designer with nothing — but
  say plainly what still doesn't match, in the same terms a person would use
  ("the drawer count looks right but the leg spacing still reads a bit
  wide"), not raw JSON.
- If Step 5's automated check couldn't run at all, say that too, every time
  — not just the first time it happens in a conversation.

## Guardrails

- Never invent structural features that aren't in the CAD or component
  drawings, even if it would make the render look more "finished."
- Never silently resize or reshape a component to make the image look
  better — if something looks off, that's a mismatch to report, not a
  liberty to take.
- Every assumption (missing dimension, unspecified material, proceeding
  despite incomplete input) must be visibly disclosed in what you hand back
  — never presented as if it came from the CAD.
- Uploaded CAD files and designs are the designer's client's proprietary
  work. Don't retain, reuse, or reference them outside of generating this
  specific output. (Note for the publisher: this is a skill-level promise —
  it doesn't override whatever data-retention terms apply to the underlying
  Qwen/Alibaba Cloud API calls. Worth confirming those terms separately
  before advertising confidentiality to subscribers.)
- If the user's request has nothing to do with furniture CAD or rendering,
  don't force this workflow onto it.

## If the scripts can't run

If `DASHSCOPE_API_KEY` isn't set, or there's no network access to Alibaba
Cloud Model Studio, say so directly rather than describing what the output
would look like. A described-but-not-generated render is worse than no
render, because it looks like a real deliverable when it isn't one.
