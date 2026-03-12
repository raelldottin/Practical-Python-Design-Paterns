# Practical Python Design Patterns
### 30-Day Flet + uv iOS Prototyping Roadmap
*Badenhorst applied through every build — Speed → Systems → Realism → Taste*

> **Book:** *Practical Python Design Patterns: Pythonic Solutions to Common Problems* — Wessel Badenhorst (2017)
> **Stack:** Python · Flet · uv
> **Duration:** 30 days · 60–90 min/day

---

## Mission

In 30 days, prototype a credible iOS-style app in Flet that a non-technical stakeholder could mistake for a real product direction — while applying every design pattern from Badenhorst directly inside the builds.

**The merge rule:** The book is the brief. The build is the lab. Every pattern gets applied as a refactor or architectural decision inside that week's Flet project. Reading without a named implementation location in your codebase does not count.

---

## Repo Structure

```
Practical-Python-Design-Patterns/
│
├── README.md                        ← you are here
├── patterns_log.md                  ← master pattern audit (updated daily)
│
├── week1-speed/                     ← Days 1–7
│   ├── day01-hello/
│   ├── day02-login/
│   ├── day03-validation/
│   ├── day04-settings/
│   ├── day05-list-detail/
│   ├── day06-refactor/
│   ├── day07-memory-test/
│   └── README.md
│
├── week2-systems/                   ← Days 8–14
│   ├── components/                  ← reusable component library (lives here permanently)
│   │   ├── __init__.py
│   │   ├── buttons.py               ← PrimaryButton, SecondaryButton
│   │   ├── cards.py                 ← CardWidget, StatTile
│   │   ├── lists.py                 ← ListRow, SectionHeader
│   │   ├── states.py                ← LoadingState, EmptyState, ErrorState
│   │   └── decorators.py           ← LoadingDecorator
│   ├── day08-audit/
│   ├── day09-buttons/
│   ├── day10-list-card/
│   ├── day11-tiles-states/
│   ├── day12-fitness-screen/
│   ├── day13-finance-dashboard/
│   ├── day14-profile-settings/
│   └── README.md
│
├── week3-realism/                   ← Days 15–21
│   ├── project/                     ← single multi-screen prototype (chosen Day 15)
│   │   ├── models/
│   │   │   └── models.py
│   │   ├── state/
│   │   │   ├── app_state.py         ← Singleton
│   │   │   └── store.py             ← Observer
│   │   ├── commands/                ← Command pattern
│   │   ├── data/
│   │   │   ├── mock_data.py
│   │   │   └── strategies.py        ← Strategy pattern
│   │   ├── persistence/
│   │   │   └── snapshot.py          ← Memento pattern
│   │   ├── views/
│   │   │   ├── screen_base.py       ← Prototype base
│   │   │   └── screen_factory.py    ← Factory pattern
│   │   └── main.py
│   └── README.md
│
├── week4-taste/                     ← Days 22–30
│   ├── capstone/                    ← polished capstone (chosen Day 22)
│   │   ├── models/
│   │   ├── views/
│   │   │   └── base_screen.py       ← Template Method
│   │   ├── controllers/
│   │   ├── state/
│   │   │   └── tab_mediator.py      ← Mediator pattern
│   │   └── main.py
│   └── README.md
│
└── Docs/
    ├── pattern-quick-reference.md
    └── architecture-notes.md        ← written Day 30
```

---

## Daily Session Structure

| Block | Time | Activity |
|---|---:|---|
| Pattern Brief | 15 min | Read the chapter. Extract one implementation target. |
| Build | 40 min | Build or refactor using that pattern in your Flet project. |
| Pattern Audit | 15 min | Name exactly where the pattern lives in your code. |

---

## patterns_log.md — The Proof File

Create this file at repo root on Day 1. Update it every session. It is the single document that proves the book and builds are merged.

| Pattern | Chapter | Week | Location in Code | Honest Assessment |
|---|---|---|---|---|
| Singleton | Ch.1 | 1 | `week3-realism/project/state/app_state.py` | |
| Prototype | Ch.2 | 1 | `week3-realism/project/views/screen_base.py` | |
| Factory | Ch.3 | 1 | `week3-realism/project/views/screen_factory.py` | |
| Facade | Ch.X | 2 | `week2-systems/components/` (entire folder) | |
| Decorator | Ch.X | 2 | `week2-systems/components/decorators.py` | |
| Composite | Ch.X | 2 | Every screen file in Week 2 | |
| Observer | Ch.X | 3 | `week3-realism/project/state/store.py` | |
| Command | Ch.X | 3 | `week3-realism/project/commands/` | |
| Strategy | Ch.X | 3 | `week3-realism/project/data/strategies.py` | |
| Memento | Ch.X | 3 | `week3-realism/project/persistence/snapshot.py` | |
| Template Method | Ch.X | 4 | `week4-taste/capstone/views/base_screen.py` | |
| MVC | Ch.X | 4 | `week4-taste/capstone/` (models/views/controllers) | |
| Mediator | Ch.X | 4 | `week4-taste/capstone/state/tab_mediator.py` | |

---

## Week-by-Week Map

### Week 1 — Speed (Days 1–7)

**Build target:** Three standalone screens: login, settings, list-detail — in clean uv project structures.
**Skill under load:** Raw build velocity. Folder structure by instinct. Flet controls without lookup.
**Patterns:** Singleton · Prototype · Factory
**Proof to unlock Week 2:** Rebuild the login screen from memory in under 20 minutes. No reference. Timed.
**Failure mode:** Spending Days 3–4 still reading docs instead of building broken things and fixing them.

| Day | Build | Pattern |
|---|---|---|
| 1 | Install uv. Create first project. Add Flet. Run default app. Build one screen: title, subtitle, one button. Ship it. | Read Ch.1 (Singleton). Note where a single app-state object could live. Don't implement yet. |
| 2 | Login screen. Email field, password field, login button. No validation. No logic. UI only. | Read Ch.2 (Prototype). Identify your base screen config as a prototype candidate. |
| 3 | Add fake validation to login. Empty email shows error text. Success state changes a visible element. | Apply Prototype: clone a base screen config object instead of rebuilding layout from scratch. |
| 4 | Settings screen. Rows: label left, toggle/chevron right. Minimum 5 rows. ListView not Column. | Read Ch.3 (Factory). Draft a screen factory function that returns configured views. |
| 5 | List-detail app. 5 hardcoded items. Tap row → detail. Back returns correct list state. | Apply Factory: `screen_factory.py` accepts a screen name and returns the configured view. It is the only entry point to views. |
| 6 | Refactor day. Pick worst build. Split into `main.py` + views file. No new features. | Apply Singleton: `app_state.py` with one state object. Import it wherever state is needed. |
| 7 | Memory test. Close everything. Rebuild login from scratch in under 20 minutes. Timed. | Pattern audit: Singleton, Prototype, Factory each have a named location in `patterns_log.md`. |

**Session check, Day 7:** If you cannot rebuild login in 20 min, repeat Days 2–3. You are not ready for Week 2.

---

### Week 2 — Systems (Days 8–14)

**Build target:** A 10-component reusable library used to assemble three distinct app screens.
**Skill under load:** Abstraction. Identifying repetition before it accumulates. Thinking in components, not controls.
**Patterns:** Facade · Decorator · Composite
**Proof to unlock Week 3:** Every screen built this week handles loading, empty, and error states. No happy-path-only screen passes.
**Failure mode:** Building components too specific to one screen. `HomeCardWidget` is not reusable. `CardWidget` with configurable props is.

| Day | Build | Pattern |
|---|---|---|
| 8 | Audit Week 1 code. List every UI pattern appearing more than once. These become component targets. | Read Facade. Recognize `components/` as a facade over raw Flet controls. Log it. |
| 9 | Build `PrimaryButton` and `SecondaryButton`. Place in `components/buttons.py`. | Read Decorator. Plan how to wrap a base button with loading-state behavior. |
| 10 | Build `ListRow` (leading icon, title, subtitle, optional trailing widget) and `CardWidget`. Both configurable for 3+ data types without modification. | Apply Decorator: `LoadingDecorator` wraps components that need a spinner state. One wrapper, reused everywhere. |
| 11 | Build `StatTile`, `EmptyState`, `LoadingState`. All must be drop-in: any screen can show them with one line. | Read Composite. Plan screens as component trees, not flat control lists. |
| 12 | Build `ErrorState`, `SectionHeader`. Library is now 10 components. Build fitness app home screen using only library components. | Apply Composite: fitness screen file contains no raw Flet controls. Every element is a composite component. |
| 13 | Finance dashboard: min 2 StatTiles, 1 CardWidget, 1 SectionHeader, 1 ListRow list. LoadingState appears 1.5s before content. | Pattern audit: Facade, Decorator, Composite all have named locations. No raw Flet control bypasses the library. |
| 14 | Profile/settings screen. EmptyState if a data section has no content. ErrorState reachable by toggle. Fix any Week 2 library-rule violations. | Final Week 2 audit: every component has a pattern justification or gets flagged in `patterns_log.md`. |

---

### Week 3 — Realism (Days 15–21)

**Build target:** One multi-screen prototype: sign-in, home feed, detail screen, editable form, local persistence, mock API data.
**Skill under load:** State architecture. Data separation. Making a prototype behave as if a backend exists.
**Patterns:** Observer · Command · Strategy · Memento
**Proof to unlock Week 4:** Every user action produces a visible UI update. State is structured, not scattered across callbacks.
**Failure mode:** State living inside control callbacks. An `on_click` that fetches data and updates six UI variables is not state management — it is chaos with indentation.

**Day 15 — commit to one project:** habit tracker / workout timer / budget tracker / book library / task planner. Do not revisit this choice.

| Day | Build | Pattern |
|---|---|---|
| 15 | Choose project. Define data models in `models.py`: one primary entity, one list state, one form state. No UI today. | Read Observer. Map it to your state-to-UI update problem. Sketch Observer mapping in `patterns_log.md`. |
| 16 | Sign-in flow using component library. On success, navigate to placeholder home screen. | Apply Observer: sign-in state lives in one state object. Button reads from it. Error message reads from it. Neither owns state directly. |
| 17 | Home feed with mock data from `mock_data.py`. LoadingState for 1 second before render. EmptyState if mock list is empty. | Apply Observer fully: UI subscribes to state changes. State changes do not call UI directly. |
| 18 | Detail screen. Navigation from list passes item data. Detail shows 4+ fields. Back preserves list scroll state. | Read Command. Every user action is a command object, not an inline callback. Draft Command location in `patterns_log.md`. |
| 19 | Editable form. Pre-fills with item data. On submit, updates in-memory list. Change reflects in list and detail without restart. | Apply Command: form submission is a `SaveItemCommand` object. Undo is optional but the structure must support it. |
| 20 | Add local persistence using `json` and `pathlib`. Load on launch. Write on every create/update/delete. Close and reopen: data survives. | Apply Memento: persistence is a memento of app state at save time. Save serializes. Load restores. |
| 21 | Replace `mock_data.py` with async function using `asyncio.sleep(1.5)`. All data-fetching moves out of view files. | Apply Strategy: `MockDataStrategy` vs. `LiveAPIStrategy`. Views call the interface. Swapping mock to live requires changing one line. |

---

### Week 4 — Taste (Days 22–30)

**Build target:** One polished capstone: tab nav, 4–6 complete screens, all states, one demo flow completable in under 60 seconds by a first-time user.
**Skill under load:** Product judgment. Knowing what to remove. Making a prototype feel like a decision, not an exercise.
**Patterns:** Template Method · MVC · Mediator
**Proof of completion:** A first-time user completes the core flow in under 60 seconds without guidance. Timed.
**Failure mode:** Polishing screens not in the demo flow. A perfect settings screen with broken onboarding is misallocated effort.

**Day 22 — commit to one capstone:** personal finance app / workout timer / note-taking app / library-study planner / meal tracker. Maximum 4 tabs. Map the 60-second demo flow on paper before writing code.

| Day | Build | Pattern |
|---|---|---|
| 22 | Map core 60-second demo flow on paper. Max 5 steps. Define tab structure (max 4 tabs, each must appear in demo flow). | Read Template Method. Draft base screen lifecycle: `init_state()`, `load_data()`, `render_content()`, `handle_error()`. |
| 23 | Set up capstone with uv. Import Week 2 component library. Build tab navigation shell. Build onboarding or sign-in screen. | Apply Template Method: every screen inherits the base lifecycle. No screen initializes, fetches, or renders outside of it. |
| 24 | Build Tab 1 fully. All states: loading, empty, error, populated. A stranger must understand this tab in under 10 seconds. | Read MVC. Tab 1 must have explicit model, view, and controller separation as folders or files — not mixed. |
| 25 | Build Tab 2 fully. Must interact with Tab 1: shared data, navigation, or state dependency. Actions in Tab 2 visible in Tab 1 without restarting. | Apply MVC to Tab 2. Draft Mediator: plan a central object for tab-to-tab communication. |
| 26 | Build Tabs 3 and 4 to functional state. Both handle all states. Identify weakest tab in demo flow — cut its scope to minimum required. | Apply Mediator: tabs communicate through a central mediator object, not directly to each other. |
| 27 | Polish — in this order only: (1) consistent spacing with one base unit, (2) one heading size, one body size, one label size, (3) remove every element not in the 60-second demo flow. | Full `patterns_log.md` review. Every pattern from all 4 weeks is named, located, and honestly assessed. |
| 28 | Add local persistence or mock backend to capstone. Core flow survives app restart. Cold-open, run demo, it works without setup. | Audit `patterns_log.md`: any pattern that feels bolted-on rather than structural gets flagged for Day 30 refactor. |
| 29 | First user test. Hand prototype to someone who has never seen it. Say nothing. Time the core flow. Write every hesitation, wrong tap, question. Fix top two friction points. | No new pattern work. Apply what the user test reveals. |
| 30 | Three tasks only: (1) Run the 60-second demo — cut until it fits. (2) Write honest self-review naming the weakest part of the capstone. (3) Execute one refactor that makes the codebase defensible to an outside reader. | Write architecture note in `patterns_log.md`: which patterns are load-bearing, which were practice, which you would apply differently. |

---

## Completion Criteria

You have completed this roadmap if and only if all of the following are true:

- A first-time user completes the core capstone flow in under 60 seconds without guidance.
- No screen in any project lacks loading, empty, and error states.
- State is structured. No action updates UI directly without going through a state object.
- The `week2-systems/components/` library is the source of all shared UI across all weeks. No duplicated control patterns exist outside it.
- You can open a blank uv project and have a running multi-screen shell within 15 minutes.
- Every pattern in `patterns_log.md` has a named file location and an honest assessment — not just a chapter reference.

---

## Pattern Quick Reference

| Pattern | Week | File Location | What It Solves |
|---|---:|---|---|
| Singleton | 1 | `week3-realism/project/state/app_state.py` | One source of truth for app-wide state |
| Prototype | 1 | `week3-realism/project/views/screen_base.py` | Clone base screen config instead of rebuilding |
| Factory | 1 | `week3-realism/project/views/screen_factory.py` | Single entry point for creating configured views |
| Facade | 2 | `week2-systems/components/` | Clean interface over raw Flet control complexity |
| Decorator | 2 | `week2-systems/components/decorators.py` | Add loading/error behavior without subclassing |
| Composite | 2 | Every screen file in Week 2 | Screens as trees of components, not flat control lists |
| Observer | 3 | `week3-realism/project/state/store.py` | UI reacts to state changes without direct coupling |
| Command | 3 | `week3-realism/project/commands/` | User actions as objects, not inline callbacks |
| Strategy | 3 | `week3-realism/project/data/strategies.py` | Swap mock vs. live data without changing views |
| Memento | 3 | `week3-realism/project/persistence/snapshot.py` | Local persistence as a serialized state snapshot |
| Template Method | 4 | `week4-taste/capstone/views/base_screen.py` | Define screen lifecycle once, override per screen |
| MVC | 4 | `week4-taste/capstone/` (models/ views/ controllers/) | Explicit separation enforced by folder structure |
| Mediator | 4 | `week4-taste/capstone/state/tab_mediator.py` | Tab communication through one central object |

---

## Hard Rules

**Behavioral patterns land in Week 3 only.** Do not force Observer, Command, or Strategy into Week 1 screens. They require real state to be meaningful. Applying Observer to a login button is practice without context.

**Banking rule.** If the pattern does not fit the current build, log it in `patterns_log.md` with the intended build noted. Apply it when the right surface exists. Forced application is worse than deferred application.

**No softening on failure.** Time spent is not proof of completion. Working artifacts that meet the criteria above are.

---

## License

Code and content provided under the [MIT License](LICENSE).