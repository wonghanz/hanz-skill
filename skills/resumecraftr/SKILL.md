---
name: resumecraftr
description: >-
  AI-powered ATS resume optimization engine. Use when the user wants to structure a CV into modular JSON sections,
  audit ATS compliance, tailor individual sections against job descriptions without inventing facts, or format resumes using minimal, modern, or executive templates.
---

# ResumeCraftr ATS Engine

ResumeCraftr provides a structured, section-by-section methodology for optimizing resumes for Applicant Tracking Systems (ATS). It enforces strict JSON schemas for CV sections, extracts verifiable achievements, and tailors content to target job descriptions while preventing AI hallucinations.

## When to Use This Skill

- Auditing and optimizing resumes for ATS parsers (Workday, Taleo, Greenhouse, Lever).
- Creating modular resume sections (Contact, Summary, Experience, Education, Skills, Projects, Certifications) from raw text or markdown.
- Tailoring specific resume sections to match job description keywords while maintaining factual integrity.
- Using structured resume templates (Minimal, Modern, Executive) and LaTeX/HTML rendering patterns.

## Core Rules & Guardrails

1. **Maintain Structural Consistency**: Treat each section as a distinct semantic block (Contact, Summary, Experience, Education, Skills, Projects).
2. **Never Invent Facts**: Strengthen wording and surface dormant skills, but never manufacture titles, companies, degrees, or metrics that the user did not provide.
3. **ATS Keyword Alignment**: Mirror exact terminology from the target Job Description (e.g., if JD specifies "Continuous Integration", do not substitute only "CI" without expanding).
4. **Action + Context + Impact**: Every bullet point must describe the action taken, tools/technologies used, and the measurable business outcome.

## CV Section Schema & Templates

Templates are available under `./templates/`:
- `resume_template.md`: Clean, markdown-based resume skeleton.
- `sections.json`: Canonical JSON structure for all resume sections.
- `minimal.html`, `modern.html`, `executive.html`: Print-optimized ATS styling templates.
- `eisvogel.latex`: LaTeX template for PDF generation.

### Section Extraction Schema

```json
{
  "Contact Information": {
    "Full Name": "string",
    "Email": "string",
    "Phone Number": "string",
    "LinkedIn": "string",
    "GitHub": "string",
    "Portfolio": "string"
  },
  "Summary": {
    "Summary": "string"
  },
  "Work Experience": [
    {
      "Job Title": "string",
      "Company": "string",
      "Location": "string",
      "Start Date": "string",
      "End Date": "string",
      "Key Responsibilities": ["string"]
    }
  ],
  "Education": [
    {
      "Degree": "string",
      "Institution": "string",
      "Location": "string",
      "Graduation Date": "string",
      "Additional Info": ["string"]
    }
  ],
  "Skills": {
    "Technical Skills": ["string"],
    "Frameworks & Tools": ["string"],
    "Soft Skills": ["string"]
  }
}
```

## Section Tailoring Workflow

When tailoring a CV section to a job description:
1. Parse the target job description to extract core competencies, required tech stack, and industry keywords.
2. Review the candidate's existing section content.
3. Rewrite the bullet points or summary to naturally weave in matching keywords where true experience exists.
4. Elevate the most relevant accomplishments to the top of each role's bullet list.
5. Provide a diff or clear before-and-after comparison.
