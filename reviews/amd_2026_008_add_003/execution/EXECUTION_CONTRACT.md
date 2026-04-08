# Execution contract — `amd_2026_008_add_003`

**Status:** draft  
**Transaction:** see `EXECUTION_TRANSACTION.json`  
**Not normative** until human review and any product merge.

---

## 1. Objective

One sentence: what this execution run must prove.

---

## 2. User-visible outcome

What a user or reviewer should be able to observe (behavior, surface, route).

---

## 3. In-scope files

| Path | Allowed change |
|------|----------------|
| | |

---

## 4. Out-of-scope / forbidden paths

| Path | Reason |
|------|--------|
| | |

---

## 5. Validation steps

| Step | Command | Expected |
|------|---------|----------|
| Install | | |
| Build | | |
| Test | | |
| Lint | (if required) | |

---

## 6. Visual proof requirements

**Required if UI/shell/canvas/routing affected.**

| Proof | Route / surface | Captured |
|-------|-----------------|----------|
| | | |

---

## 7. Known risks

- 

---

## 8. Stop conditions

When to stop the run without promotion (e.g. build fails, scope creep, missing proof).

- 

---

## 9. Validation commands (MVP runner)

Optional file **`VALIDATION_COMMANDS.json`** in this same folder overrides defaults for **[`scripts/run_isolated_execution_demo.py`](../../../scripts/run_isolated_execution_demo.py)**.

Shape:

```json
{
  "install": ["npm", "ci"],
  "build": ["npm", "run", "build"],
  "test": ["npm", "test", "--", "--run", "inSource"]
}
```

Each value is a **non-empty argv list** (no shell). Omitted keys skip that step. If the file is absent, the runner uses **`npm ci`**, **`npm run build`**, **`npm test -- --run inSource`** when **`package.json`** exists in the product repo.
