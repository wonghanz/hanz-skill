# Required credentials

This Skill is built for Capafy's **Run Online — Subscription** mode. Every
API credential below is supplied once by the publisher during
`publish-configure` (Capafy stores it in its encrypted vault and injects it
at runtime) — subscribers never see it, never supply their own, and never
need a DashScope account.

| Env var | Service | Used for |
|---|---|---|
| `DASHSCOPE_API_KEY` | Alibaba Cloud Model Studio (DashScope) — Qwen-VL, Qwen-Image, Qwen-Image-Edit | Every step of the pipeline: input validation, structure extraction, rendering, consistency checking, and edit-based retries. See `scripts/*.py` — all read this single variable via `os.environ.get("DASHSCOPE_API_KEY")`. |

No other credentials are required. This Skill never needs access to a
designer's own accounts, cloud storage, or any service beyond generating
renders from the images they upload in the conversation.

**Cost note for the publisher**: because this key is yours, every
subscriber run is billed to your DashScope account (up to ~4 generation
calls per angle per version, plus vision calls — see SKILL.md Step 3-5).
Price the subscription with that per-run cost in mind.
