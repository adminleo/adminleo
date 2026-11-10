## Leonardo Bornhäußer

[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--6464--5179-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0005-6464-5179)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24100702-1682D4?style=flat-square)](https://doi.org/10.5281/zenodo.24100702)
[![CV](https://img.shields.io/badge/CV-adminleo.github.io%2Fcv-24292F?style=flat-square&logo=github&logoColor=white)](https://adminleo.github.io/cv/)

Managing director and CTO at [Creativate Technologies](https://creativate.tech),
Berlin. I build AI systems that have to justify their answers — knowledge-graph
grounding, provenance, audit trails — mostly for finance, legal and public-sector
users who cannot accept "the model said so".

Currently formalising the analytics side of that work: statistics, experimental
design, and SQL that holds up under scrutiny rather than just returning rows.

### Here

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

**[eniac-magist-analysis](https://github.com/adminleo/eniac-magist-analysis)**
&nbsp;![SQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Tableau](https://img.shields.io/badge/-Tableau-E97627?style=flat-square&logo=tableau&logoColor=white)

Should a European electronics retailer enter Brazil through a logistics partner?
A SQL analysis of 99,441 marketplace orders, ending in a recommendation that
contradicts the deal on the table. Every figure traces back to the query that
produced it, and the repository is explicit about the one question the data
cannot answer. `challenge/` adds an interview-style exercise on the same
database, where the headline finding is that 56 % of reviewers write no text at
all and still average 4.38 stars — which quietly inflates any keyword-sentiment
comparison built on that table.

**[sql-foundations](https://github.com/adminleo/sql-foundations)**
&nbsp;![SQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

Eighty-nine queries on the `publications` schema, from `SELECT` to chained joins
and royalty tiers. Each one executed against the database by a verifier rather
than only written; the comments carry the reasoning, including the NULL and
`BETWEEN` traps that quietly produce wrong answers.

**[ab-testing](https://github.com/adminleo/ab-testing)**
&nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)

A sample-size calculator and a design checklist. Standard library only, with
tests against known quantiles. Mostly it exists to make one relationship
obvious: halving the effect you want to detect quadruples the traffic you need.

### Working with

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![pandas](https://img.shields.io/badge/-pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/-AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)

Seven, not seventy — these are the ones I would be happy to be tested on.
Alongside them: Next.js in production, Postgres and SQLite, graph stores, and a
long-standing preference for systems that can show their work.

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
