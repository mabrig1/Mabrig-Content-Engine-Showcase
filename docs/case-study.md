# Engineering case study: Content Engine

## Problem
Creators and agencies need to coordinate drafts, approvals, schedules and publishing without confusing a scheduled job with a successful delivery.

## Approach
Separate content creation from external publishing, use explicit approval gates, preserve job status and validate timestamps. A production design should include authenticated accounts, idempotent jobs, retry limits and provider-specific delivery evidence.

## Portfolio evidence
The independent example uses synthetic post records and demonstrates an approval and scheduling gate. It neither calls AI providers nor connects to social accounts or publishes posts. The original documentation describes CRM, content scheduling and analytics; production availability and performance are not independently verified here.

## Interview topics
Queue design, state transitions, tenant isolation, OAuth boundaries, asynchronous jobs and automated tests.
