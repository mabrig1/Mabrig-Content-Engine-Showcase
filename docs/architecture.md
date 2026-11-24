# Conceptual content workflow architecture

```mermaid
flowchart LR
 A[Content brief] --> B[Draft workspace]
 B --> C[Human approval]
 C --> D[Scheduled job]
 D --> E[Private publishing gateway]
 E --> F[Delivery evidence and review]
```

This conceptual diagram is not production topology. Original project documentation describes Next.js, TypeScript, PostgreSQL, Prisma, Redis queues and optional AI and social integrations. Live posting and provider connectivity have not been independently verified. Credentials, private prompts, customer records and production implementation are excluded.
