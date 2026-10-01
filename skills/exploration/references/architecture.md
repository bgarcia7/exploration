# Architecture and technical design

Covers system architecture, service boundaries, data models and storage, sync and offline strategies, API design, choosing between algorithms or approaches, infrastructure layout, and refactor or migration strategies.

## What the seed is for here

Engineers anchor on the first familiar pattern. Here the seed makes you take credible alternatives seriously, ones you'd otherwise dismiss without a second look. **It does not pick the answer.** Every candidate has to be viable, and the final recommendation is made on merit. It may well be the conventional option. What the user gets is a real comparison instead of a single default.

The comparison is the point, so make **three candidates by default**. If the user asked for one design, still compare it against the obvious baseline.

## Fixed vs open

**Usually fixed:** functional requirements, hard non-functional ones (latency targets, budget, compliance, offline support, data residency), stack commitments the user named, team size and skills if known, and correctness.

**Usually open:** which quality attribute leads, how the system is split up, data ownership and storage, the consistency model, how parts communicate, the deployment shape, build vs. buy, and one deliberately imposed constraint.

## Reading the seed

Lean on indexing. Walk the digit sequence: each digit picks an entry from the next menu. If a pick contradicts a fixed requirement or makes an incoherent pair with an earlier pick, skip to the next digit and note the skip. Use the letters only for color, such as naming the direction.

**Lead quality**
0 simplicity / fewest moving parts · 1 cost · 2 latency · 3 throughput and scale · 4 reliability and failure isolation · 5 evolvability / speed of change · 6 operability and debuggability · 7 security and privacy · 8 offline / local-first · 9 testability and developer experience

**Shape**
0 single process · 1 modular monolith · 2 services by domain · 3 event-driven / log-centric · 4 serverless functions · 5 local-first with sync (CRDT or similar) · 6 batch pipeline · 7 actor model · 8 ports-and-adapters core · 9 client-heavy with a thin backend

**Data**
0 one relational database · 1 document store · 2 event sourcing · 3 CQRS read models · 4 key-value plus cache · 5 object storage as the database · 6 embedded database per client (SQLite) · 7 graph · 8 append-only log · 9 managed backend-as-a-service

**Imposed constraint** (a design-thinking lever; drop it if it fights a fixed requirement)
0 no new infrastructure · 1 no background jobs · 2 runs on one machine · 3 zero server-side session state · 4 every write idempotent · 5 one data store total · 6 everything replayable · 7 no third-party services · 8 ships as a single artifact · 9 works with the network off

## Building

For each candidate:

- A short description and a diagram (Mermaid or ASCII).
- How it meets each fixed requirement, or where it strains.
- Key trade-offs, failure modes, operational cost, and a rough effort estimate.
- What would have to be true for this one to win.

Give each candidate its best version, with no strawmen. Then add a comparison table across the qualities that matter for this problem and a recommendation with reasons. A hybrid or the boring option is a fine recommendation. Write a spike sketch only if it settles a question; don't write production code unless asked.

## Deliverable

A design doc or a reply containing the candidates, the diagrams, the comparison table, and the recommendation. The seed and the menu picks stay out of the doc.
