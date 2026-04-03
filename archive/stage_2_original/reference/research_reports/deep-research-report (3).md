# Migrating to the New AI OS: Step-by-Step Plan

To safely transform the current monolithic repo into a lean, containerized **AI OS**, we must proceed incrementally.  We should start by mapping everything (as we already did), then extract only the *core* pieces and rebuild them one “slice” at a time.  The high-level steps are:

1. **Inventory Core Components and Schema** – Map out the existing runtime, DB schema, and invariant tables.
2. **Define Minimal Schema & Contracts** – Strip down to only the essential tables and formalize the “intent‐execution” contract.
3. **Refactor Server into Execution Gateways** – Reorganize routes around a unified execution API rather than feature endpoints.
4. **Containerize the Core Services** – Build a Docker image (and Compose) for the core OS with Node and Postgres.
5. **Test & Deploy the Base System** – Write integration tests and CI pipelines to validate the OS, then spin up a base Docker instance.
6. **Phase-by-Phase Migration** – Use the Strangler Pattern to replace old features with new slices (one domain or surface at a time)【5†L51-L59】【2†L158-L166】.

Each step below elaborates on these phases.

## 1. Inventory Core Components and Schema
Before cutting anything, **catalog the existing system**.  Document every runtime entrypoint, schema table, and “frozen” component (voice pipeline, Twilio webhooks, etc.) that actually *runs* the AI OS (this is already partially done). Key pieces to enumerate include:
- **Database schema:** Tables like `site_configs`, `agents`, `intent_executions`, `customer_accounts`, `telephony_configs`, etc.  Treat `shared/schema.ts` + `migrations/` as the ground truth for Postgres. Every core entity (site identity, agent identity, intents, call logs, chat logs, etc.) should be noted.  
- **Core services:** Identify all server modules (e.g. `server/index.ts`, `server/storage.ts`, `server/routes.ts` and its subrouters) and their responsibilities.  Note which functions are pure infrastructure (e.g. `geminiVoice`, Twilio streams) vs. product logic.  
- **Client surfaces:** Note the main app shell (`client/App.tsx`) and key UI components (chat interface, Concierge panel, voice widget).  These are our canvases but only matter after the backend is in place.  
- **Governance artifacts:** Catalog rules and registries (YAML or MD) that constrain behavior.  These don’t run code directly, but they define allowed execution paths.  

This comprehensive inventory is essentially an architecture document: listing each component, its files, interactions, and data flows.  (In practice, teams sometimes write architecture docs with diagrams to capture this–see e.g. methods in architecture inventories【14†L252-L261】.)  The goal is to know exactly what *must* be re-implemented in the new OS core and what can be deferred as an extension.

## 2. Define a Minimal Schema and Canonical Contracts
Next, **extract the bare database and runtime contracts** that the OS needs.  This means pruning all but the essential tables and defining a strict execution model (“kernel interface”):

- **Canonical Execution Contract:**  Formalize a JSON schema or TypeScript interface for the intent loop. For example, define an `IntentExecution` record (with fields like `intentId`, `actor`, `allowedSkills`, `selectedSkill`, `action`, `outcome`, etc.).  Store only what’s needed: inputs, chosen skill, action result, and audit trail.  In the new OS, *every* action must pass through this contract (no ad hoc side-effects).  Using JSON Schema or TypeScript types makes this explicit【16†L219-L223】. In practice, these contracts become our “api”. For example, an HTTP POST `/api/execute-intent` might accept the intent ID and context, then return a standardized outcome payload.  

- **Minimal Database Schema:**  Based on the inventory, **strip down to core tables**. Likely candidates: `sites` (or `site_configs`), `agents`, `sessions`, `intent_executions` (or `work_items`), plus any tables absolutely needed for login/OTP.  Remove any tables that only support legacy features or optional extensions.  Use domain-driven design (DDD) to guide what stays: each bounded context (e.g. Voice, SMS, Chat, Agent framework) should eventually own its own subset of data.  This avoids a single mega-database. Domain-driven techniques like event-storming can help identify these boundaries【5†L84-L93】.  For now, ensure the core OS data (identities, intents, outcomes) have a clean, normalized schema. Preserve migrations for incremental updates.  

- **Anti-Corruption & ACLs:**  Decide on any “anti-corruption layers.”  For instance, during migration, old code might need to call new code – use an adapter so the old schema (if still present) isn’t directly mixed with the new one【5†L100-L106】.  Likewise, all calls between services should use your canonical contract or an API gateway (see next section).  

Think of this step as **drawing up the kernel of the OS**: only the identity, intent, skill, and outcome models (and minimal support tables like `sessions` or `api_keys`).  Everything else (detailed voice logs, elaborate telephony records, etc.) can be added later.

## 3. Refactor Server into Execution Gateways 
With the core concepts defined, reorganize the backend around *execution flows* instead of ad-hoc feature routes.  In the new OS, **all actions should funnel through one or few gateways** that enforce the OS contract:

- **API Gateway:** Create a central entry point (e.g. `/api/execute-intent`, `/api/canvas-control`, or a GraphQL gateway) that receives high-level commands (intent invocations, view navigations, etc.). This gateway handles auth, validation, and routing. In effect it becomes the OS’s “kernel interface,” dispatching to the right service or skill.  This is analogous to an API Gateway in microservices, which performs schema validation and traffic routing【16†L85-L93】. (For example, an incoming intent might hit `/api/execute-intent` with a validated JSON body; the gateway checks permissions, then passes it to the Intent Executor service.)

- **Move Business Routes to Services:**  Each functional area (e.g. user/agent management, telephony config, chat logs, code-intents, etc.) should become its own service or module that implements the standardized interface.  For instance, instead of having `/api/intelligence` and `/api/coding-intents` mounted side-by-side in one big Express router, those become separate handler functions or microservices behind the gateway.  The legacy `server/routes.ts` mounting can be reduced to just a few top-level routers (health, gateway, admin).

- **Express Route Refactor:** In practice, this might look like replacing many `app.use(…)` in `server/routes.ts` with a single handler for the gateway, plus a couple of support routes (e.g. for health checks, billing).  All internal feature logic moves under that gateway or behind it.  For example, instead of hitting `/api/workspace/onboarding` directly, a client might send an “enter workspace” intent to the gateway, which then loads configuration and returns the initial canvas state. 

- **Governance Enforcement:** Tie the registry rules into the gateway logic.  For example, when the gateway receives a “navigate” or “invoke” command, it should consult the logical route registry to check if that action is allowed (instead of relying on React routes).  In other words, the server becomes the arbiter of allowed flows. This makes governance runtime-enforced rather than just documentation.

This effectively turns the backend into a small *orchestrator* that routes intent/actions to skills.  It also sets up the architecture for independent deployment: each domain can be its own service.  As one guidance says, **“structure the application as a set of independently deployable, loosely coupled components”**【22†L190-L199】. The figure below illustrates a typical microservice-like decomposition:

【34†embed_image】 *Figure:* Example of a microservice-style decomposition. Each bounded-context (subdomain) is an independent service owned by a team, all coordinated via an API gateway【22†L190-L199】. In our OS, this means splitting the code by domain (Auth, Chat, Voice, Telephony, etc.) with one unified entrypoint.

## 4. Containerize the Core Services
With code refactored, package it in Docker. The goal is a **lean, reproducible image** for the OS core:

- **Base Image & Multi-stage Build:** Use a lightweight Node base (e.g. `node:20-alpine`) and a multi-stage Dockerfile to install only production dependencies【27†L967-L972】【20†L128-L136】.  For example, one stage can use a full Node image to build assets, then copy compiled files into an `alpine`-based image. Multi-stage builds keep secrets out and minimize final size【27†L967-L972】.

- **Production Dependencies Only:** Ensure `npm install` (or `pnpm/`yarn) is run with `--production` in the final image, so dev-tools don’t bloat the container【9†L254-L263】.  This might mean copying `package.json` and doing `npm ci --omit=dev` in the Dockerfile.

- **Docker Compose (Optional):** For development and CI, create a `docker-compose.yml` that brings up the Node service *and* a PostgreSQL container together (possibly with a volume).  Set environment variables like `DATABASE_URL=postgres://…` so the app can connect.  This makes it trivial to spin up a full local stack.  For example: 
  ```yaml
  services:
    api:
      build: . 
      ports: ["3000:3000"] 
      environment: [NODE_ENV=development, DATABASE_URL=postgres://...]
      depends_on: [postgres]
    postgres:
      image: postgres:15
      environment: [POSTGRES_USER=postgres, POSTGRES_PASSWORD=postgres, POSTGRES_DB=ai_os]
      volumes: [pgdata:/var/lib/postgresql/data]
  volumes:
    pgdata:
  ```
  (Similar setups are common in Node+Postgres Docker guides【20†L178-L187】.)

- **CI Pipeline Build:** Integrate the Docker build into CI. Each commit to main should trigger a Docker build (and publish to a registry if desired). Enforce pinned base-image tags (e.g. `node:20.9-alpine`) to avoid drifting【9†L276-L284】.

- **Environment and Secrets:** Use Docker ARG/ENV judiciously. Do **not** bake secrets into the image. Leverage multi-stage to keep tokens out of final layers【27†L967-L972】. For local dev, a `.env` file or Compose can supply secrets. For production, use your orchestration secrets management (Kubernetes secrets, GitHub Actions secrets, etc.) when building/deploying.

By containerizing early, we ensure the new OS can be deployed anywhere with Docker.  We should verify that simply running `docker-compose up` (or `docker run`) brings up the OS with a fresh database (using the Drizzle migrations) and that the core API responds.

## 5. Test & Deploy the Base System
Before declaring the new OS ready, **validate it end-to-end**:

- **Automated Testing:**  Build a comprehensive test suite for the core logic.  This includes *unit tests* for each service, *integration tests* that spin up the container and hit the HTTP/WebSocket interfaces, and (if feasible) simple end-to-end flows.  For instance, a test might set up a demo site, create an intent execution, and verify the outcome matches expectations. Microservices best practices call for CI/CD pipelines that run these tests on every change【12†L126-L135】.  Adopt “shift-left” testing: add tests as soon as you build each new API route【12†L57-L66】【12†L126-L135】.

- **Contract Testing:** Since services will talk through APIs, use contract tests (e.g. Pact) to lock down interface agreements.  This ensures that as you refactor, you don’t accidentally break expected request/response shapes【12†L181-L188】.

- **Service Virtualization:** If needed, mock external dependencies (e.g. actual Twilio, Gemini, or external MCP services) during testing. This allows isolated testing of the core OS without relying on third-party availability【12†L103-L112】.

- **Staging/Smoke Tests:** Before any “go-live,” run a staging version of the container with real Postgres and simulate key operations (agent login, initiate chat, perform an intent, make a mock call). Perform smoke tests and sanity checks to catch integration issues. Tools like curl, Postman, or automated scripts can drive these flows.  Testing in a production-like environment helps ensure the OS’s contract is solid.

- **Observability:** Add logging and metrics to verify the OS is working as intended. For example, log each intent execution path and compare counts or flows to the old system during a parallel run (see next step).

## 6. Phased Migration Strategy
Finally, **roll out the new OS slice by slice** using the Strangler Fig pattern【5†L51-L59】【2†L158-L166】. Do *not* switch everything at once. Instead:

- **Identify Slices:** Divide the functionality into logical slices (e.g. Authentication & Authorization, Chat text UI, Voice pipeline, SMS compliance, Coding-intents, etc.). Each slice should be a complete, end-to-end feature or domain that can be moved separately. For example, first migrate the **public agent chat** flow as a slice, then move **voice calls**, then **telephony billing**, and so on.

- **Proxy/Gateway Routing:** Implement an API gateway or router that can send certain requests to the old code or the new service. Initially, all traffic goes to the old system. As you finish each slice, flip the gateway to route those intents/paths to the new container instead. This is classic Strangler technique: gradually envelop the old system with the new one【5†L51-L59】【2†L158-L166】.

- **Parallel Running:** For critical functions, consider running the new OS in parallel with the old system (the “parallel run” pattern). For a period, send the same inputs to both and compare outputs (without yet exposing the new one to end-users). This verifies parity. Tools like contract testing or duplicate logging can help compare results【2†L180-L189】.

- **Data Migration:** For shared data (e.g. user accounts), ensure the new OS can read existing tables or vice versa. You might sync certain tables or maintain compatibility. Eventually, decommission old tables as the new services take over. Carefully plan any schema changes with migrations and possibly data-copy steps between Postgres instances if needed.

- **Validation and Rollback:** After each slice goes live, monitor closely. Validate business metrics (calls handled, chats served, etc.) match expectations. Have a rollback plan to route traffic back to the old code if something breaks.

Over time, the gateway will route more and more functionality to the new OS container, until the legacy monolith is unused and can be retired. This approach minimizes risk and aligns with best practices: “a big bang rewrite is risky; instead, incrementally add new services around the existing app and swap them in”【5†L51-L59】【2†L158-L166】. 

---

Throughout this migration, remember that the goal is a **clean, minimal AI OS kernel**. Everything we put into the container should serve that core OS purpose. We already know the system has all the pieces we need (voice pipeline, chat UI, etc.) – now we must *rebuild* them in an ordered, disciplined way. By following this plan — inventorying and pruning, refactoring into clear contracts, containerizing with best practices, and iteratively switching over features — we’ll end up with a deployable Docker image of the new AI OS base. From there we can build out the remaining features and scale safely. 

**Sources:** The above strategy follows standard incremental migration patterns (Strangler Fig)【5†L51-L59】【2†L158-L166】, microservices design principles【22†L190-L199】, and Docker best practices (multi-stage builds, CI/CD)【27†L967-L972】【12†L126-L135】. The importance of JSON schemas and a unified gateway for an “AI OS” has also been noted in recent AI architecture discussions【16†L85-L93】【16†L219-L223】. Each phase here is guided by those industry-proven approaches.