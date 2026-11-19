<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/career-dark.png">
  <img src="assets/career-light.png" alt="Career: consultant 2019–2021, proxy product owner at Karla / Sparkassen-Finanzgruppe 2021–2022, co-founder and head of operations at Camsol 2022–2025, managing director and CTO at Creativate Technologies since 2024">
</picture>

[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6464--5179-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0005-6464-5179)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24100702-1682D4?style=flat-square)](https://doi.org/10.5281/zenodo.24100702)
[![CV](https://img.shields.io/badge/CV-adminleo.github.io%2Fcv-24292F?style=flat-square&logo=github&logoColor=white)](https://adminleo.github.io/cv/)

I consult on AI projects, build the systems, and ship my own products where the
case holds up. Managing director and CTO at
[Creativate Technologies](https://creativate.tech) in Frankfurt, where the work
is knowledge-graph grounding, provenance and audit trails — mostly for finance,
legal and public-sector users who cannot accept "the model said so".

Technical product owner by trade: requirements, prioritisation, architecture
decisions, the release gate, and the conversation with the people who have to
sign off. Most of that work is under NDA or not released yet. What is here is
the part that can be shown, and a theme runs through it: the headline number is
usually the one to distrust, and most of the effort goes into finding out
whether it means anything.

---

## Products and platforms I have owned

| | |
|---|---|
| **c:node** · 2024 – now<br>founder, architect, lead | Knowledge-graph decision intelligence: bind a language model to a store that can be checked, so answers are auditable rather than fluent. In 2026 the monolith (~258,000 lines) was replaced by a service platform with its own identity and billing services. Runs in the cloud or fully on-premise with local GPU inference. |
| **Zulano** · 2026 – now<br>architecture and ontology | Application and funding assistant for the public sector. A data mesh of more than 34 million structured records as the grounding layer, and a rule-based Java/Spring Boot service that routes a request to the responsible authority deterministically — a decision that may not depend on a model's guess. |
| **LeadScout · Claudio · AI&nbsp;Playbook** · 2025 – 2026<br>founder, lead | Three product bets taken to paying customers: a multi-tenant B2B lead engine with ICP scoring and CRM integrations, a voice-note-to-task assistant shipped as SaaS and as a signed desktop app, and a trilingual AI-readiness check that generates its report as a PDF and sells in two tiers. Positioning, pricing and service boundaries owned end to end; folded into c:node in 2026 once the market had answered. |
| **Gasvisor** · 2022 – 2024<br>venture lead | IoT CO₂ monitoring for industry: battery-powered LTE-M sensors for fill level, temperature and humidity, cloud analytics, and a dashboard with consumption forecast and automatic re-ordering — built for TRGS-510 compliance and ESG reporting, taken from incubator MVP to enterprise customers. |
| **CheckMe** · 2023 – 2025<br>venture lead | Breast-cancer early detection for underserved regions: native apps plus web, an AI companion, and ultrasound analysis producing a radiologist-reviewed BI-RADS report. Clinical and regulatory stakeholders, privacy by design for health data. |
| **Karla** · 2021 – 2022<br>proxy product owner | Beyond-banking platform of the German savings banks group, mandated by the DSGV. Headless CMS and a multi-vendor commerce layer, integrated with the Java systems of the group's IT provider. Requirements from three shareholder savings banks consolidated against one backlog and prepared for committee decision; a joint board pitch secured €500,000. |

Before all of that: first technical lead in 2014, and a decade of software
projects since. The full account is in the [CV](https://adminleo.github.io/cv/).

---

## Where it actually runs

I deploy and then operate — the thing that breaks on a Sunday is mine.

- **AWS** — EC2 with Docker behind Caddy and automatic TLS, S3 and CloudFront,
  Lambda, ECR with lifecycle policies, Route 53, security groups opened and
  closed per session. Day-to-day over the CLI, not the console.
- **Google Cloud** — Cloud Functions on a schedule, behind Cloud SQL over a
  unix socket, secrets in Secret Manager, Cloud Scheduler authenticating with
  OIDC. The public receipt for this one is
  [gans-data-pipeline](https://github.com/adminleo/gans-data-pipeline), including
  the deploy and teardown scripts and the four permission mistakes they now
  avoid.
- **Hetzner** — smaller services and staging where the cost per gigabyte of RAM
  decides it.
- **On-premise and air-gapped** — single-command deployment on a customer's own
  hardware with local GPU inference, for buyers whose data cannot leave the
  building. One pilot ran on a German city's live data.

What I have not done, in case it saves someone a call: no managed Kubernetes in
production, and no Bedrock.

---

## Research

**[grounded-ai-evals](https://github.com/adminleo/grounded-ai-evals)**
&nbsp;[![tests](https://img.shields.io/github/actions/workflow/status/adminleo/grounded-ai-evals/tests.yml?style=flat-square&label=tests)](https://github.com/adminleo/grounded-ai-evals/actions)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24100702-1682D4?style=flat-square)](https://doi.org/10.5281/zenodo.24100702)

How do you test a system whose job is to answer *with evidence*? Four layers,
ordered so that each one is only meaningful once the one above it holds. The
library computes the metrics and renders a release gate that blocks on named
checks rather than on a weighted mean.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/eval-gate-dark.png">
  <img src="assets/eval-gate-light.png" alt="The four layers, and a release gate that blocks on three named checks while the system passes both baselines">
</picture>

The example run is the argument for the design: a system that beats a plain
model and ordinary RAG, and is still blocked, by name, on provenance coverage,
citation precision and unsupported-claim rate. An average would have let it
through. Standard library, tested, with the method mapped to public standards
and to the EU AI Act articles the evidence serves.

Also public:
**[governed-graph-growth](https://github.com/CreativateLabs/governed-graph-growth)**
&nbsp;[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24099664-1682D4?style=flat-square)](https://doi.org/10.5281/zenodo.24099664)
— a technical note on letting a knowledge graph grow without letting it rot.
Next: evaluation methods for AI that answers with evidence, and point-in-time
legal grounding. Papers in preparation; artefacts land here first.

---

## Public code

### Pipelines

**[gans-data-pipeline](https://github.com/adminleo/gans-data-pipeline)**
&nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![GCP](https://img.shields.io/badge/-Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

Scrapes city facts, weather and arriving flights into SQL on a daily schedule —
local first, then the same function on Cloud Functions behind Cloud SQL, with a
[live page](https://adminleo.github.io/gans-data-pipeline/) that reads a
published snapshot so the database keeps no public route. The population column
turned out to be the interesting part: Wikipedia uses six different labels for
it across seven cities and dates them from a 2006 census to 2026, so a hardcoded
label returns nothing for four of them — silently, as a missing value.

### Models, and the metrics that mislead

**[ames-house-prices](https://github.com/adminleo/ames-house-prices)**
&nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

Is this house expensive, and what is it worth? Answering "no" to every house is
right 85.1 % of the time and finds none of them, so the work is in the metrics
that survive a 14.9 % positive rate.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/ames-errors-dark.png">
  <img src="assets/ames-errors-light.png" alt="Both error groups sit within $17,420 of the price cutoff that defines the label">
</picture>

Every mistake sits next to the cutoff that *defined* the label — so predicting
the price and applying the rule afterwards beats classifying directly, F1 0.843
against 0.813 over the same 20 folds (p = 0.0098). Also: grid search scored on
its own folds inflates F1 by 0.027 for a tree and 0.000 for a linear model.

**[moosic-playlists](https://github.com/adminleo/moosic-playlists)**
&nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

Can K-Means turn Spotify audio features into playlists? The features carry real
similarity — a song's nearest neighbours share its artist 19.5× more often than
chance — but the clusters describe how a track was *recorded*, not how it feels:
of 92 titles recorded by two different artists, only 23.9 % land together.
Forget to scale and the eight clusters come out as a ladder of track length,
2.6 to 61.7 minutes, with no error raised.

### Analysis that ends in a decision

**[eniac-magist-analysis](https://github.com/adminleo/eniac-magist-analysis)**
&nbsp;![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Tableau](https://img.shields.io/badge/-Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)

Should a European retailer enter Brazil through a logistics partner? 99,441
marketplace orders, ending in a recommendation that contradicts the deal on the
table. Every figure traces to the query that produced it, and the repository is
explicit about the one question the data cannot answer.

**[eniac-discount-strategy](https://github.com/adminleo/eniac-discount-strategy)**
&nbsp;![pandas](https://img.shields.io/badge/-pandas-150458?style=flat-square&logo=pandas&logoColor=white)

Cleaning a corrupted retail dataset, where the interesting question is which
corruptions can be repaired and which cannot. Three columns look repairable and
are not — and proving it moves a headline number by a factor of ten. A blanket
divisor reproduced the undamaged rows' ratio to the price paid almost exactly
while listing a MacBook Pro at €35,255.

### Foundations

**[sql-foundations](https://github.com/adminleo/sql-foundations)** — eighty-nine
queries from `SELECT` to chained joins, each executed against the database by a
verifier rather than only written. ·
**[ab-testing](https://github.com/adminleo/ab-testing)** — a sample-size
calculator and a design checklist, existing mostly to make one relationship
obvious: halving the effect you want to detect quadruples the traffic you need.

---

## How I work

**Set the threshold before the run.** A bar agreed afterwards is a description,
not a test. `Check` takes the measured value and the bar in the same call so a
scorecard cannot be assembled to flatter the result, and an unmeasured check
fails closed. — [grounded-ai-evals](https://github.com/adminleo/grounded-ai-evals)

**Ask what the metric is actually measuring.** Clusters that look like genres
and turn out to be recording conditions; an F1 that moves because the label was
drawn with a ruler. Both only showed up once the evaluation was aimed at the
claim instead of the model. —
[moosic-playlists](https://github.com/adminleo/moosic-playlists),
[ames-house-prices](https://github.com/adminleo/ames-house-prices)

**Say which question the data cannot answer.** Writing that line down is
usually the most useful paragraph in a report, and the one most often left out.
— [eniac-magist-analysis](https://github.com/adminleo/eniac-magist-analysis)

**Prefer a loud failure to a quiet one.** A hardcoded label that returns nothing
costs more than a crash, because nobody goes looking. Every fallback in these
repositories reports what it did not recognise. —
[gans-data-pipeline](https://github.com/adminleo/gans-data-pipeline)

---

## Working with

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/-AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![GCP](https://img.shields.io/badge/-Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

Eight, not eighty — the ones I would be happy to be tested on. Alongside them:
pandas and scikit-learn, Postgres and SQLite, graph stores, Java and Spring Boot
at architecture level, Ollama for local inference, and a long-standing
preference for systems that can show their work.

<details>
<summary>Activity</summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=adminleo&theme=github_dark">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=adminleo&theme=github" alt="Profile summary">
</picture>

</details>

[CV](https://adminleo.github.io/cv/) ·
[creativate.tech](https://creativate.tech) ·
[LinkedIn](https://www.linkedin.com/in/leonardo-bornhaeusser) ·
[ORCID](https://orcid.org/0009-0005-6464-5179)
