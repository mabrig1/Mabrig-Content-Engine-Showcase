# MABRIG Content Engine | Engineering Portfolio

**Content automation · Social media workflow design · SaaS engineering**

[Developer profile](https://github.com/mabrig1) · [MABRIG Technologies](https://www.mabrigkorie.org)

Content Engine is a social media CRM and content automation project. Its original documentation describes scheduling, content generation, CRM, analytics and platform integrations using Next.js, TypeScript, PostgreSQL, Prisma and Redis. Live integrations, production availability and performance have not been independently verified here.

## Explore the portfolio

- [Conceptual architecture](docs/architecture.md)
- [Engineering case study](docs/case-study.md)
- [Interactive simulated publishing queue](demo/index.html) — download and open locally in a browser.
- [Independent Python scheduling example](demo/scheduling.py)
- [Automated tests](demo/test_scheduling.py)
- [CI workflow](.github/workflows/demo.yml)

## Reproduce the example

```sh
python demo/scheduling.py
python -m unittest discover -s demo -v
```

Python 3.10+; no dependencies or credentials. The examples use fictional records and demonstrate approval gates, timezone-aware scheduling and explicit job states. They do not generate content with AI, connect social accounts or publish anything.

## Engineering competencies

Asynchronous workflow design, approval boundaries, input validation, queue eligibility, timezone handling, data privacy and automated testing.

## Intellectual property and technical review

See [NOTICE.md](NOTICE.md). Original production code, private prompts, customer data, credentials and social integrations are excluded. Recruiters may contact MABRIG Technologies for a guided demonstration or scoped technical discussion.
