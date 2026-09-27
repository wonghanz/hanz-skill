# Hanz Skill Vault 🚀

> A curated collection of 35 enterprise-grade agent skills, career optimization engines, security sentinels, and creative multi-modal pipelines designed for **Google Antigravity**, **Claude Code**, **Codex**, and modern AI coding assistants.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Skills Catalog](#skills-catalog)
  - [🛡️ Security & Cyber-Defense Suite (4)](#-security--cyber-defense-suite)
  - [💼 Career, Resume & Job Search Suite (27)](#-career-resume--job-search-suite)
  - [🎨 Design, Video & Multi-Modal Suite (4)](#-design-video--multi-modal-suite)
- [Installation & Quick Start](#installation--quick-start)
  - [Google Antigravity](#google-antigravity)
  - [Claude Code / OpenCode / Codex](#claude-code--opencode--codex)
  - [Workspace-Specific Setup](#workspace-specific-setup)
- [Repository Structure](#repository-structure)
- [Security & DLP Compliance](#security--dlp-compliance)
- [License](#license)

---

## 🌟 Overview

Each skill in this repository is packaged according to the modern Agent Skill specification:
- **`SKILL.md`**: Standard frontmatter with title, scope description, triggers, and comprehensive execution instructions.
- **Reference & Template Assets**: Schemas, guides, LaTeX templates, rulebooks, and prompts.
- **Runnable Scripts**: Standalone automation pipelines and test utilities (where applicable).

---

## 📦 Skills Catalog

### 🛡️ Security & Cyber-Defense Suite

| Skill | Description | Key Capabilities |
| :--- | :--- | :--- |
| [`aegis-guard`](skills/aegis-guard/) | Enterprise-grade AI Cybersecurity Sentinel | Anti-Fable 5 adversarial injection defense, Zero-Leak DLP policy, blast-radius verification. |
| [`open-source-security-contribution`](skills/open-source-security-contribution/) | Open-source security fix contribution pipeline | Issue discovery and ranking by learning value, isolated local reproduction, failing regression test, minimal fix, three human approval gates before commit/push/PR. |
| [`nodiguard`](skills/nodiguard/) | Zero-trust local AI security proxy & system optimizer | Hardcoded secret neutralization, tokenized prompt isolation, memory safety enforcement. |
| [`security-audit`](skills/security-audit/) | Rigorous multi-phase codebase security audit | 13 attack classes, machine-readable finding ledgers, Cloudflare edge rule validation, automated reporting. |

---

### 💼 Career, Resume & Job Search Suite

| Skill | Description | Highlights |
| :--- | :--- | :--- |
| [`academic-cv-builder`](skills/academic-cv-builder/) | Academic CV formatting & builder | Publications, grant proposals, teaching dossier, and tenure-track CV structuring. |
| [`application-form-filler`](skills/application-form-filler/) | Intelligent job application field filler | Context-aware, tailored answers mapped directly from candidate profile and JD. |
| [`career-changer-translator`](skills/career-changer-translator/) | Cross-industry skill translator | Identifies transferable competencies, reframes prior achievements for new target domains. |
| [`cold-email-writer`](skills/cold-email-writer/) | High-conversion cold outreach writer | Crafts concise, human, personalized outreach to founders and hiring managers. |
| [`cover-letter-generator`](skills/cover-letter-generator/) | Targeted cover letter generator | Compelling narrative bridge between resume achievements and job descriptions. |
| [`creative-portfolio-resume`](skills/creative-portfolio-resume/) | Creative resume builder | Balances visual design flair with strict ATS parseability for designers and artists. |
| [`executive-resume-writer`](skills/executive-resume-writer/) | C-suite & VP executive resume writer | Emphasizes P&L ownership, board-level communication, and enterprise vision. |
| [`interview-coach`](skills/interview-coach/) | Full-cycle high-rigor interview coach | Rubric scoring, storybank manager, mock drills across PM, Eng, Design, Data, and Ops. |
| [`interview-prep-generator`](skills/interview-prep-generator/) | Targeted interview preparation | Formulates STAR stories, expected technical/behavioral questions, and talking points. |
| [`job-description-analyzer`](skills/job-description-analyzer/) | Deep job posting analyzer | Calculates match score, uncovers unspoken requirements, and flags critical qualification gaps. |
| [`linkedin-profile-optimizer`](skills/linkedin-profile-optimizer/) | LinkedIn profile optimization | Recruiter SEO keywords, headline hooks, punchy "About" copy, and featured work curation. |
| [`offer-comparison-analyzer`](skills/offer-comparison-analyzer/) | Total compensation & offer evaluator | Side-by-side equity, base, bonus, vesting cliffs, tax implications, and benefits comparison. |
| [`portfolio-case-study-writer`](skills/portfolio-case-study-writer/) | Portfolio deep-dive case study writer | Expands bullet points into full narrative case studies (Problem, Discovery, Solution, Impact). |
| [`reference-list-builder`](skills/reference-list-builder/) | Professional reference manager | Formats professional references and equips referees with prep kits and talking points. |
| [`repo-to-resume`](skills/repo-to-resume/) | Codebase-to-Resume extractor | Mines GitHub repositories for evidence-based bullet points; compiles live LaTeX resumes. |
| [`resume`](skills/resume/) | Master career & resume coordinator | Orchestrates all resume lifecycle sub-skills based on user goals and workflow phase. |
| [`resume-ats-optimizer`](skills/resume-ats-optimizer/) | ATS scanner & keyword optimization | Keyword frequency scoring, ATS parser compatibility checks, format sanitization. |
| [`resume-bullet-writer`](skills/resume-bullet-writer/) | Impact-driven bullet point writer | Transforms passive job duties into metric-anchored achievement bullets (X-Y-Z formula). |
| [`resume-formatter`](skills/resume-formatter/) | Layout & visual hierarchy formatter | Clean scannable layouts, ATS compliance, font hierarchy, and whitespace balance. |
| [`resume-quantifier`](skills/resume-quantifier/) | Metric & impact quantification | Discovers hidden opportunities for metrics and guides realistic estimation frameworks. |
| [`resume-section-builder`](skills/resume-section-builder/) | Modular resume section builder | Customizes Education, Skills, Experience, and Project sections by seniority level. |
| [`resume-tailor`](skills/resume-tailor/) | Job-specific resume tailoring | Surgically aligns existing experience with specific target job postings without hallucination. |
| [`resume-version-manager`](skills/resume-version-manager/) | Resume version tracking & control | Maintains master source-of-truth resume while managing specialized variant branches. |
| [`resumecraftr`](skills/resumecraftr/) | Modular JSON-driven resume engine | JSON-first CV architecture, instant schema validation, and exportable modern templates. |
| [`salary-negotiation-prep`](skills/salary-negotiation-prep/) | Salary & compensation negotiation | Market compensation research, negotiation strategy playbooks, and counter-offer scripts. |
| [`tech-resume-optimizer`](skills/tech-resume-optimizer/) | Tech industry resume optimizer | Tailored specifically for Software Engineers, Tech Leads, Engineering Managers, and PMs. |
| [`technical-job-search`](skills/technical-job-search/) | Full technical job search copilot | End-to-end guidance from initial application to final offer negotiation. |

---

### 🎨 Design, Video & Multi-Modal Suite

| Skill | Description | Key Capabilities |
| :--- | :--- | :--- |
| [`apple-design`](skills/apple-design/) | Apple design system & fluid motion | Physical spring animations, gesture-driven UI, translucent materials, and Apple typography. |
| [`furniture-cad-render`](skills/furniture-cad-render/) | Automated furniture CAD photorealistic render pipeline | Multi-angle CAD drawing analysis, Qwen-VL/Image pipeline, automated consistency verification. |
| [`remotion-best-practices`](skills/remotion-best-practices/) | Remotion React video production standards | 30+ production rules covering composition, animations, audio, captions, and rendering. |
| [`rentguard-ai`](skills/rentguard-ai/) | RentGuard AI 租房合同霸王条款透视镜 | Multi-modal OCR contract scanner, PRC Civil Code compliance, risk scoring, and counter-tactics. |

---

## 🛠️ Installation & Quick Start

### Google Antigravity

To make these skills available globally to Antigravity:
```bash
# Clone the repository
git clone https://github.com/wonghanz/hanz-skill.git

# Copy any (or all) skills into your global Antigravity skills directory
cp -r hanz-skill/skills/* ~/.gemini/config/skills/
```

### Claude Code / OpenCode / Codex

To install for Claude Code or other compatible agents:
```bash
cp -r hanz-skill/skills/<skill-name> ~/.claude/skills/
# or
cp -r hanz-skill/skills/<skill-name> ~/.codex/skills/
```

### Workspace-Specific Setup

Drop the desired skill directory directly into your project's `.gemini/skills/` or `.agent/skills/` folder:
```bash
mkdir -p my-project/.gemini/skills
cp -r hanz-skill/skills/security-audit my-project/.gemini/skills/
```

---

## 📁 Repository Structure

```
hanz-skill/
├── .gitignore
├── README.md
└── skills/
    ├── academic-cv-builder/
    ├── aegis-guard/
    ├── apple-design/
    ├── application-form-filler/
    ├── career-changer-translator/
    ├── cold-email-writer/
    ├── cover-letter-generator/
    ├── creative-portfolio-resume/
    ├── executive-resume-writer/
    ├── furniture-cad-render/
    ├── interview-coach/
    ├── interview-prep-generator/
    ├── job-description-analyzer/
    ├── linkedin-profile-optimizer/
    ├── nodiguard/
    ├── offer-comparison-analyzer/
    ├── portfolio-case-study-writer/
    ├── reference-list-builder/
    ├── remotion-best-practices/
    ├── rentguard-ai/
    ├── repo-to-resume/
    ├── resume/
    ├── resume-ats-optimizer/
    ├── resume-bullet-writer/
    ├── resume-formatter/
    ├── resume-quantifier/
    ├── resume-section-builder/
    ├── resume-tailor/
    ├── resume-version-manager/
    ├── resumecraftr/
    ├── salary-negotiation-prep/
    ├── security-audit/
    ├── tech-resume-optimizer/
    └── technical-job-search/
```

---

## 🔒 Security & DLP Compliance

This repository strictly adheres to **NodiGuard Zero-Leak Data Loss Prevention (DLP)** standards:
- **No hardcoded secrets**: All API keys, passwords, bearer tokens, and private credentials are excluded.
- **Environment decoupled**: Any scripts require environment variables (`os.environ.get(...)`) supplied at runtime.
- **Strict `.gitignore`**: Local `.env`, credentials files, logs, and development artifacts are automatically filtered.

---

## 📄 License

Private repository curated for personal and team agent orchestration.
