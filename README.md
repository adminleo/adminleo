## Leonardo Bornhäußer

Managing director and CTO at [Creativate Technologies](https://creativate.tech),
Berlin. I build AI systems that have to justify their answers — knowledge-graph
grounding, provenance, audit trails — mostly for finance, legal and public-sector
users who cannot accept "the model said so".

Currently formalising the analytics side of that work: statistics, experimental
design, and SQL that holds up under scrutiny rather than just returning rows.

### Here

**[eniac-magist-analysis](https://github.com/adminleo/eniac-magist-analysis)** —
Should a European electronics retailer enter Brazil through a logistics partner?
A SQL analysis of 99,441 marketplace orders, ending in a recommendation that
contradicts the deal on the table. Every figure traces back to the query that
produced it, and the repository is explicit about the one question the data
cannot answer.

**[sql-foundations](https://github.com/adminleo/sql-foundations)** —
Eighty-nine queries on the `publications` schema, from `SELECT` to chained joins
and royalty tiers. Each one executed against the database by a verifier rather
than only written; the comments carry the reasoning, including the NULL and
`BETWEEN` traps that quietly produce wrong answers.

**[ab-testing](https://github.com/adminleo/ab-testing)** —
A sample-size calculator and a design checklist. Standard library only, with
tests against known quantiles. Mostly it exists to make one relationship
obvious: halving the effect you want to detect quadruples the traffic you need.

### Working with

SQL and Python for analysis · FastAPI and Next.js in production · Postgres,
SQLite, graph stores · Docker on AWS · and a long-standing preference for
systems that can show their work.

### Elsewhere

[creativate.tech](https://creativate.tech) ·
[LinkedIn](https://www.linkedin.com/in/leonardo-bornhaeusser)
