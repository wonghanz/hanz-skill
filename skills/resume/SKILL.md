---
name: resume
description: >-
  Master resume and career skill coordinator. Use this skill whenever the user asks for resume help, CV writing,
  tailoring, ATS optimization, bullet points, cover letters, career transitions, interview coaching, or salary negotiation.
  Orchestrates specialized skills across the resume lifecycle.
---

# Resume & Career Master Hub

Welcome to the central command hub for all resume, career development, interview preparation, and job application workflows. When a user requests help with resumes or career transitions, this skill serves as the primary navigator and coordinates the specialized sub-skills installed in the system.

## Specialized Skills Index

Choose the specialized skill based on the user's specific request:

| User Need | Recommended Skill | When to Activate |
| :--- | :--- | :--- |
| **Comprehensive Resume Writing & Review** | `resume` | General resume requests, initial audits, or multi-step resume overhauls. |
| **ATS Optimization & Scoring** | `resume-ats-optimizer` or `resumecraftr` | Checking ATS compliance, keyword match scores, avoiding ATS rejection traps. |
| **Tailor Resume to Job Description** | `resume-tailor` or `technical-job-search` | Customizing an existing resume for a specific job posting. |
| **Turn GitHub Repo/Code into Resume** | `repo-to-resume` | Extracting real, honest, evidence-grounded bullets from code repositories. |
| **Transform Bullet Points** | `resume-bullet-writer` | Rewriting bullets using XYZ (Accomplished [X] as measured by [Y] by doing [Z]). |
| **Add Metrics & Numbers** | `resume-quantifier` | Estimating or uncovering quantifiable business impact and performance metrics. |
| **Software Engineer / Tech Resumes** | `tech-resume-optimizer` | Specialized formatting and terminology for SWE, DevOps, Cloud, AI, and Data roles. |
| **Executive / Leadership Resumes** | `executive-resume-writer` | C-Suite, VP, Director resumes emphasizing strategic vision and P&L impact. |
| **Career Change / Industry Transition** | `career-changer-translator` | Re-framing transferable skills and overcoming non-traditional backgrounds. |
| **Academic CVs** | `academic-cv-builder` | Publications, grants, teaching experience, research statements. |
| **Creative & Design Portfolios** | `creative-portfolio-resume` | Balancing visual layout with ATS scannability for UX/UI and designers. |
| **Cover Letters** | `cover-letter-generator` | Generating targeted, compelling cover letters matching the JD. |
| **Job Description Breakdown** | `job-description-analyzer` | Deconstructing job postings into must-haves, nice-to-haves, and match scores. |
| **Interview Coaching & Mock Practice** | `interview-coach` | Full mock interviews, STAR/CAR framework, rubrics, and feedback. |
| **Quick Interview Questions from Resume**| `interview-prep-generator` | Generating expected behavioral and technical questions based on CV. |
| **Salary & Compensation Negotiation** | `salary-negotiation-prep` | Researching market compensation, counter-offer scripts, equity/RSUs. |
| **Compare Multiple Job Offers** | `offer-comparison-analyzer` | Side-by-side total comp analysis, benefits evaluation, and decision frameworks. |
| **Cold Outreach & Networking Emails** | `cold-email-writer` | Concise, personalized emails to hiring managers, founders, and recruiters. |
| **Job Application Questions** | `application-form-filler` | Writing answers to application portal questions and essays. |
| **LinkedIn Profile Optimization** | `linkedin-profile-optimizer` | Aligning LinkedIn headlines, summaries, and experience with resumes. |
| **Portfolio Case Studies** | `portfolio-case-study-writer` | Turning project bullets into in-depth engineering/design case studies. |
| **Resume Formatting & Layout** | `resume-formatter` | Structuring clean, human-readable, and machine-scannable layouts. |
| **Resume Version Management** | `resume-version-manager` | Managing master vs. targeted resume versions across different roles. |
| **Reference List Preparation** | `reference-list-builder` | Organizing professional reference sheets and outreach etiquette. |

---

## Standard Workflow for a Resume Request

When a user provides a resume or asks to build one:

### Step 1: Intake & Triage
1. **Identify the user's role and target**:
   - Role type: Software Engineer, Executive, Career Changer, Academic, Creative, General.
   - Purpose: General review, specific job application, ATS check, or rewrite.
2. **Review existing material**:
   - If they have a repo or codebase: invoke `repo-to-resume`.
   - If they have a job description: invoke `job-description-analyzer` or `resume-tailor`.
   - If they have an existing resume: inspect structure, bullets, and formatting.

### Step 2: Content Optimization
1. **Bullet Point Construction**: Apply the Google XYZ formula via `resume-bullet-writer`:
   - *"Accomplished [X], as measured by [Y], by doing [Z]"*.
2. **Metric Injection**: Use `resume-quantifier` to surface latency improvements, revenue, team size, uptime, or cost savings.
3. **Keyword Alignment**: Use `resume-ats-optimizer` and `resumecraftr` to ensure industry-standard keywords are naturally included.

### Step 3: Formatting & Presentation
1. Structure into standard ATS sections:
   - Header (Name, Phone, Email, Location, LinkedIn, GitHub/Portfolio)
   - Professional Summary (Optional, 2-3 high-impact lines)
   - Technical Skills (Categorized by Languages, Frameworks, Cloud/Tools)
   - Professional Experience (Reverse-chronological)
   - Projects (Especially for junior to mid-level SWEs)
   - Education & Certifications
2. Verify ATS safety: single-column layout, standard fonts, no tables/graphics/columns that break parsers.

### Step 4: Next Steps & Application Support
Once the resume is ready, offer downstream support:
- Cover Letter: `cover-letter-generator`
- Cold Outreach: `cold-email-writer`
- Interview Prep: `interview-coach` or `interview-prep-generator`
- Offer Negotiation: `salary-negotiation-prep`
