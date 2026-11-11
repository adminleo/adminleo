## Leonardo Bornhäußer

[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6464--5179-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0005-6464-5179)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24100702-1682D4?style=flat-square)](https://doi.org/10.5281/zenodo.24100702)
[![CV](https://img.shields.io/badge/CV-adminleo.github.io%2Fcv-24292F?style=flat-square&logo=github&logoColor=white)](https://adminleo.github.io/cv/)

Managing director and CTO at [Creativate Technologies](https://creativate.tech),
Berlin. I build AI systems that have to justify their answers — knowledge-graph
grounding, provenance, audit trails — mostly for finance, legal and public-sector
users who cannot accept "the model said so".

The repositories below are the analytics side of that work. A theme runs through
them: the headline number is usually the one to distrust, and most of the effort
goes into finding out whether it means anything.

### Research

**[grounded-ai-evals](https://github.com/adminleo/grounded-ai-evals)**
&nbsp;[![tests](https://img.shields.io/github/actions/workflow/status/adminleo/grounded-ai-evals/tests.yml?style=flat-square&label=tests)](https://github.com/adminleo/grounded-ai-evals/actions)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24100702-1682D4?style=flat-square)](https://doi.org/10.5281/zenodo.24100702)

How do you test a system whose job is to answer *with evidence*? A four-layer
method — graph correctness, ontology hygiene, answer groundedness, baseline
comparison — ordered so each layer is only meaningful once the one above it
holds. The library computes the metrics and renders a release gate that blocks
on named checks rather than a weighted mean, because a 0.91 composite can hide
a 0.40 unsupported-claim rate. Standard library, tested, with the method mapped
to public standards and to the EU AI Act articles the evidence serves.

### Machine learning

**[ames-house-prices](https://github.com/adminleo/ames-house-prices)**
&nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

Is this house expensive, and what is it worth? Answering "no" to every house is
right 85.1 % of the time and finds none of them, so the work is in the metrics
that survive a 14.9 % positive rate. The errors turn out to sit within $17,000
of the cut-off that *defined* the label — so predicting the price and applying
the rule afterwards beats classifying directly, F1 0.843 against 0.813 on the
same 20 folds (p = 0.0098). Also: grid search scored on its own folds inflates
F1 by 0.027 for a tree and 0.000 for a linear model.

**[moosic-playlists](https://github.com/adminleo/moosic-playlists)**
&nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

Can K-Means turn Spotify audio features into playlists? The features carry real
similarity — a song's nearest neighbours share its artist 19.5× more often than
chance — but the clusters describe how a track was *recorded*, not how it feels:
of 92 titles recorded by two different artists, only 23.9 % land together.
Forget to scale and the eight clusters come out as a ladder of track length,
2.6 to 61.7 minutes, with no error raised.

### Data analysis

**[eniac-discount-strategy](https://github.com/adminleo/eniac-discount-strategy)**
&nbsp;![pandas](https://img.shields.io/badge/-pandas-150458?style=flat-square&logo=pandas&logoColor=white)

Cleaning a corrupted retail dataset, where the interesting question is which
corruptions can be repaired and which cannot. Three columns look repairable and
are not — and proving it moves a headline number by a factor of ten. A blanket
divisor reproduced the undamaged rows' ratio to the price paid almost exactly
while listing a MacBook Pro at €35,255.

**[eniac-magist-analysis](https://github.com/adminleo/eniac-magist-analysis)**
&nbsp;![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Tableau](https://img.shields.io/badge/-Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)

Should a European retailer enter Brazil through a logistics partner? 99,441
marketplace orders, ending in a recommendation that contradicts the deal on the
table. Every figure traces to the query that produced it, and the repository is
explicit about the one question the data cannot answer.

### Foundations

**[sql-foundations](https://github.com/adminleo/sql-foundations)** — eighty-nine
queries from `SELECT` to chained joins, each executed against the database by a
verifier rather than only written. ·
**[ab-testing](https://github.com/adminleo/ab-testing)** — a sample-size
calculator and a design checklist, existing mostly to make one relationship
obvious: halving the effect you want to detect quadruples the traffic you need.

### Working with

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![pandas](https://img.shields.io/badge/-pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/-AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)

Eight, not eighty — the ones I would be happy to be tested on. Alongside them:
Next.js in production, Postgres and SQLite, graph stores, and a long-standing
preference for systems that can show their work.

### Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=adminleo&theme=github_dark">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=adminleo&theme=github" alt="Profile summary">
</picture>

### Elsewhere

[CV](https://adminleo.github.io/cv/) ·
[creativate.tech](https://creativate.tech) ·
[LinkedIn](https://www.linkedin.com/in/leonardo-bornhaeusser) ·
[ORCID](https://orcid.org/0009-0005-6464-5179)
