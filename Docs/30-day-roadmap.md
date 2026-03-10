# 30-DAY FLET + UV

# iOS PROTOTYPING ROADMAP

Merged with Practical Python Design Patterns

Badenhorst — Applied Through Every Build

**Speed → Systems → Realism → Taste**

---

# MISSION & OPERATING RULES

## MISSION

In 30 days, prototype a credible iOS-style app in Flet that a non-technical stakeholder could mistake for a real product direction — while applying every design pattern from *Practical Python Design Patterns* (Badenhorst) directly inside the builds.

## THE MERGE RULE

The book is the brief. The build is the lab. Every pattern gets applied as a refactor or architectural decision inside that week's Flet project. Reading without a named implementation location in your codebase does not count.

## Daily Session Structure (60–90 min)

| Block | Time | Activity |
|---|---:|---|
| Pattern Brief | 15 min | Read the chapter. Extract one implementation target. |
| Build | 40 min | Build or refactor using that pattern in your Flet project. |
| Pattern Audit | 15 min | Name exactly where the pattern lives in your code. |

## The patterns_log.md File (Add to Every Project)

Create this file at the root of every project. It is your proof that the book and builds are merged:

| Pattern | Chapter | Location in Code | Honest Assessment |
|---|---|---|---|
| Singleton | Ch.1 | state/app_state.py | Works. Would structure differently next time. |
| Factory | Ch.3 | views/screen_factory.py | Eliminated 40 lines of conditional navigation. |
| Observer | Ch.X | state/store.py | Required — UI must not update state directly. |

## PATTERN-TO-WEEK MAP

| Week | Roadmap Focus | Patterns That Belong Here |
|---|---|---|
| Week 1 | Speed / Structure | Singleton, Prototype, Factory |
| Week 2 | Components / Systems | Decorator, Facade, Composite |
| Week 3 | State / Data / Realism | Observer, Command, Strategy, Memento |
| Week 4 | Polish / Architecture | Template Method, MVC, Mediator |

## HARD RULE: Behavioral Patterns Land in Week 3 Only

Do not force Observer, Command, or Strategy into Week 1 screens. They require real state to be meaningful. Applying Observer to a login button is practice without context.

## BANKING RULE: If the pattern does not fit the current build, log it

Add the pattern name, chapter, and intended build to patterns_log.md. Apply it when the right surface exists. Forced application is worse than deferred application.

---

# WEEK 1 — SPEED

| Dimension | Detail |
|---|---|
| Build Target | Three standalone screens: login, settings, list-detail — in clean uv project structures. |
| Skill Under Load | Raw build velocity. Folder structure by instinct. Flet controls without lookup. |
| Patterns This Week | Singleton (app state), Prototype (screen cloning), Factory (screen creation) |
| Proof to Unlock Week 2 | Rebuild the login screen from memory in under 20 minutes. No tabs. No reference. Timed. |
| Most Likely Failure Mode | Spending Days 3–4 still reading docs instead of building broken things and fixing them. |
| Refactor for Mastery | After first working login screen, strip to minimum controls that still function. Remove anything not load-bearing. |

## Day 1

**Build:** Install uv. Create first project. Add Flet. Run the default app. Build one screen: title, subtitle, one button. It does nothing. Ship it anyway.

**Pattern:** Read Ch. 1 (Singleton). Note where a single app-state object could live. Don't implement yet.

**End-of-Session Check:** App runs from uv run. Folder is clean.

## Day 2

**Build:** Build a login screen. Email field, password field, login button. No validation. No logic. UI only.

**Pattern:** Read Ch. 2 (Prototype). Identify your base screen config as a prototype candidate.

**End-of-Session Check:** Layout holds at 400x800 simulated mobile size.

## Day 3

**Build:** Add fake validation to login. If email is empty, show error text. Hardcoded check is fine.

**Pattern:** Apply Prototype: clone a base screen config object instead of rebuilding layout from scratch for each new screen.

**End-of-Session Check:** Error state is visible. Success state navigates or changes a visible element.

## Day 4

**Build:** New project. Build settings screen. Rows with label left, toggle/chevron right. Minimum 5 rows. Use ListView not Column if content might overflow.

**Pattern:** Read Ch. 3 (Factory). Draft a screen factory function that returns configured views.

**End-of-Session Check:** Toggles update their own state when tapped.

## Day 5

**Build:** New project. List-detail app. 5 hardcoded items. Tapping a row navigates to detail. Back returns to correct list state.

**Pattern:** Apply Factory: implement a screen_factory.py function that accepts a screen name and returns the configured view.

**End-of-Session Check:** Back navigation preserves list state. Factory function is the only entry point to views.

## Day 6

**Build:** Refactor Day. Pick worst of your three builds. Split into minimum two files: main.py and a views file. No new features. Structural cleanup only.

**Pattern:** Apply Singleton: create app_state.py with a single app-state object. Import it wherever state is needed.

**End-of-Session Check:** App runs identically after the split. Singleton is in patterns_log.md with its location named.

## Day 7

**Build:** Memory test. Close everything. Rebuild login screen from scratch in under 20 minutes. No reference. Timed.

**Pattern:** Pattern audit: open patterns_log.md, verify Singleton, Prototype, and Factory each have a named location in code.

**End-of-Session Check:** If you cannot rebuild in 20 min, repeat Days 2–3. You are not ready for Week 2.

---

# WEEK 2 — SYSTEMS

| Dimension | Detail |
|---|---|
| Build Target | A 10-component reusable library used to assemble three distinct app screens. |
| Skill Under Load | Abstraction. Identifying repetition before it accumulates. Thinking in components, not controls. |
| Patterns This Week | Facade (component library as interface), Decorator (wrapping controls with state behavior), Composite (screens as component trees) |
| Proof to Unlock Week 3 | Every screen built this week handles loading, empty, and error states without being asked. No happy-path-only screen passes. |
| Most Likely Failure Mode | Building components too specific to one screen. HomeCardWidget is not reusable. CardWidget with configurable props is. |
| Refactor for Mastery | After building all three screens, find every place you copied-and-adjusted instead of importing-and-configuring. Collapse those into the library. |

## Day 8

**Build:** Audit Week 1 code. List every UI pattern appearing more than once. These become component targets.

**Pattern:** Read Facade pattern. Recognize your component library as a facade over raw Flet controls. Name it as one in patterns_log.md.

**End-of-Session Check:** Component target list exists. Facade entry is logged.

## Day 9

**Build:** Build PrimaryButton (label + on_click) and SecondaryButton. Place in components/ folder.

**Pattern:** Read Decorator pattern. Plan how to wrap a base button with loading-state behavior.

**End-of-Session Check:** Both components import cleanly into a blank screen.

## Day 10

**Build:** Build ListRow (leading icon, title, subtitle, optional trailing widget) and CardWidget (title, body, optional footer). Both must be configurable for 3+ data types without modification.

**Pattern:** Apply Decorator: wrap LoadingDecorator around components that need a spinner state. One wrapper, reused everywhere.

**End-of-Session Check:** LoadingDecorator is in patterns_log.md. It wraps at least one component.

## Day 11

**Build:** Build StatTile (metric + value + optional trend), EmptyState (icon + message + optional CTA), LoadingState (spinner + optional message).

**Pattern:** Read Composite pattern. Plan screens as composite trees of components, not flat control lists.

**End-of-Session Check:** EmptyState and LoadingState are drop-in. Any screen can show them with one line.

## Day 12

**Build:** Build ErrorState (message + retry), SectionHeader (label + optional action). Library is now 10 components. Build a fitness app home screen using only library components.

**Pattern:** Apply Composite: the fitness screen file contains no raw Flet controls. Every element is a composite component.

**End-of-Session Check:** Screen file imports only from components/. Composite is named in patterns_log.md.

## Day 13

**Build:** Build finance dashboard: minimum 2 StatTiles, 1 CardWidget, 1 SectionHeader, 1 ListRow list. LoadingState appears for 1.5 seconds before content renders.

**Pattern:** Pattern audit: all three patterns (Facade, Decorator, Composite) have named locations. Verify no raw Flet control bypasses the library on any screen built this week.

**End-of-Session Check:** LoadingState delay works. Finance screen uses library only.

## Day 14

**Build:** Build profile/settings screen. Must include EmptyState if a data section has no content. ErrorState must be reachable by a toggle. Refactor: fix any Week 2 library-rule violations.

**Pattern:** Final Week 2 audit: every component has a pattern justification or gets flagged in patterns_log.md as needing one.

**End-of-Session Check:** All three screens pass the all-states requirement. patterns_log.md is current.

---

# WEEK 3 — REALISM

| Dimension | Detail |
|---|---|
| Build Target | One multi-screen prototype: sign-in, home feed, detail screen, editable form, local persistence, mock API data. |
| Skill Under Load | State architecture. Data separation. Making a prototype behave as if a backend exists. |
| Patterns This Week | Observer (state-to-UI binding), Command (user actions as objects), Strategy (swappable data sources), Memento (persistence as state snapshot) |
| Proof to Unlock Week 4 | Every user action produces a visible UI update. No silent results. State is structured, not scattered across callbacks. |
| Most Likely Failure Mode | State living inside control callbacks. An on_click that fetches data and updates six UI variables is not state management. It is chaos with indentation. |
| Refactor for Mastery | After prototype works, move all state into a single state object or class. Views read from it. Actions write to it. Nothing else. |

## Project Choice — Commit on Day 15

Pick one: habit tracker / workout timer / budget tracker / book library / task planner. Do not revisit this choice.

## Day 15

**Build:** Choose and commit to your Week 3 project. Define data models in models.py: one primary entity, one list state, one form state. No UI today.

**Pattern:** Read Observer pattern. Map it to your state-to-UI update problem. Identify which state changes need to notify which views.

**End-of-Session Check:** models.py exists. Observer mapping is sketched in patterns_log.md.

## Day 16

**Build:** Build sign-in flow using component library. On success, navigate to placeholder home screen.

**Pattern:** Begin applying Observer: sign-in state lives in one state object. Button reads from it. Error message reads from it. Neither owns state directly.

**End-of-Session Check:** Sign-in state has a single owner. No state in UI callbacks.

## Day 17

**Build:** Build home feed/dashboard with mock data from mock_data.py. LoadingState for 1 second before render. EmptyState if mock list is empty.

**Pattern:** Apply Observer fully: UI subscribes to state changes. State changes do not call UI directly.

**End-of-Session Check:** EmptyState and LoadingState work. Observer pattern is named in patterns_log.md with its location.

## Day 18

**Build:** Build detail screen. Navigation from list passes item data. Detail shows 4+ fields. Back action preserves list scroll state.

**Pattern:** Read Command pattern. Every user action is a command object, not an inline callback.

**End-of-Session Check:** Back navigation preserves list state. Command pattern location is drafted in patterns_log.md.

## Day 19

**Build:** Build editable form screen. Pre-fills with item data. On submit, updates in-memory list. Change reflects in list and detail without app restart.

**Pattern:** Apply Command: form submission is a SaveItemCommand object. Undo capability is optional but the structure must support it.

**End-of-Session Check:** Submitted updates persist within session. Command class exists in code.

## Day 20

**Build:** Add local persistence using json and pathlib. Load on launch. Write on every create/update/delete. Close and reopen: data survives.

**Pattern:** Read and apply Memento: persistence is a memento of app state at save time. The save function serializes state. The load function restores it.

**End-of-Session Check:** Data survives app restart. Memento is named and located in patterns_log.md.

## Day 21

**Build:** Replace mock_data.py with async function using asyncio.sleep(1.5). All data loading goes through this function. Move all data-fetching calls out of view files.

**Pattern:** Read and apply Strategy: data-fetching strategy is swappable (MockDataStrategy vs. LiveAPIStrategy). Views call the interface. They do not know which strategy runs.

**End-of-Session Check:** Strategy pattern is in patterns_log.md. Swapping mock to live requires changing one line, not ten.

---

# WEEK 4 — TASTE

| Dimension | Detail |
|---|---|
| Build Target | One polished capstone: tab nav, 4–6 complete screens, all states, one demo flow completable in under 60 seconds by a first-time user. |
| Skill Under Load | Product judgment. Knowing what to remove. Making a prototype feel like a decision, not an exercise. |
| Patterns This Week | Template Method (screen lifecycle), MVC (explicit folder separation), Mediator (tab-to-tab communication) |
| Proof of Completion | A first-time user completes the core flow in under 60 seconds without any guidance. Timed. |
| Most Likely Failure Mode | Polishing screens not in the demo flow. Perfect settings screen with broken onboarding is misallocated effort. |
| Refactor for Mastery | After first user test, delete or stub everything outside the core 60-second flow. Complexity not serving the demo is debt. |

## Capstone Project Choice — Commit on Day 22

Pick one: personal finance app / workout timer app / note-taking app / library-study planner / meal tracker. Maximum 4 tabs. Map the 60-second demo flow on paper before writing code.

## Day 22

**Build:** Choose capstone. Map core 60-second demo flow on paper. Max 5 steps. Define tab structure (max 4 tabs, each must appear in demo flow).

**Pattern:** Read Template Method. Plan a base screen lifecycle that every screen overrides: init_state(), load_data(), render_content(), handle_error().

**End-of-Session Check:** Demo flow exists on paper. Template Method base class is drafted.

## Day 23

**Build:** Set up capstone project with uv. Import Week 2 component library. Build tab navigation shell (placeholder screens). Build onboarding or sign-in screen.

**Pattern:** Apply Template Method: every screen inherits the base lifecycle. No screen initializes, fetches, or renders outside of it.

**End-of-Session Check:** All tabs load without errors. Every screen inherits the template. Pattern is named in patterns_log.md.

## Day 24

**Build:** Build Tab 1 fully. All states: loading, empty, error, populated. A stranger must understand this tab in under 10 seconds.

**Pattern:** Read MVC. Tab 1 must have explicit model, view, and controller separation as folders or files, not mixed.

**End-of-Session Check:** Tab 1 passes all-states requirement. model/view/controller separation is visible in file structure.

## Day 25

**Build:** Build Tab 2 fully. Must interact with Tab 1 (shared data, navigation, or state dependency). Actions in Tab 2 visible in Tab 1 without restarting.

**Pattern:** Apply MVC to Tab 2. Read Mediator pattern. Plan a central mediator for tab-to-tab communication.

**End-of-Session Check:** Tab 2 updates Tab 1 state correctly. Mediator class is drafted in patterns_log.md.

## Day 26

**Build:** Build Tabs 3 and 4 to functional state. Both handle all states. Identify weakest tab in demo flow and cut its scope to the minimum required.

**Pattern:** Apply Mediator: tabs communicate through a central mediator object, not directly to each other.

**End-of-Session Check:** All 4 tabs are functional. Mediator is in code and named in patterns_log.md.

## Day 27

**Build:** Polish day — in this order only: (1) consistent spacing with one base unit, (2) typography: one heading size, one body size, one label size — nothing else, (3) remove every element not in the 60-second demo flow or a required state.

**Pattern:** Full patterns_log.md review. Every pattern from all 4 weeks is named, located, and honestly assessed.

**End-of-Session Check:** No spacing inconsistencies. No elements outside demo flow. patterns_log.md is complete.

## Day 28

**Build:** Add local persistence or mock backend to capstone. Core flow survives app restart. Open cold, run demo, it works without setup.

**Pattern:** Pattern implementation audit: re-read each pattern entry in patterns_log.md. Any that feel bolted-on rather than structural get flagged for Day 30 refactor.

**End-of-Session Check:** Data persists. Cold-start demo works cleanly.

## Day 29

**Build:** First user test. Hand prototype to someone who has never seen it. Say nothing. Time the core flow. Write every hesitation, wrong tap, and question. Fix the top two friction points.

**Pattern:** No new pattern work today. Apply what the user test reveals.

**End-of-Session Check:** User test notes are written. Top two fixes are implemented before Day 30.

## Day 30

**Build:** Three tasks only: (1) Run the 60-second demo — cut until it fits. (2) Write honest self-review naming the weakest part of the capstone. (3) Execute one refactor that makes the codebase defensible to an outside reader.

**Pattern:** Write a one-page architecture note in patterns_log.md: which patterns are load-bearing, which were practice, which you would apply differently.

**End-of-Session Check:** Demo runs in under 60 seconds. Self-review is written. Architecture note exists.

---

# COMPLETION CRITERIA

You have completed this roadmap if and only if all of the following are true:

- A first-time user completes the core capstone flow in under 60 seconds without guidance.
- No screen in any project lacks loading, empty, and error states.
- State is structured. No action updates UI directly without going through a state object.
- Your component library is the source of all shared UI. No duplicated control patterns exist outside it.
- You can open a blank uv project and have a running multi-screen shell within 15 minutes.
- Every pattern in patterns_log.md has a named file location and an honest assessment — not just a chapter reference.

## FAILURE CONDITION — No Softening

Spending 30 days on this material and still hardcoding state, still building screens without empty and error behavior, still duplicating UI instead of componentizing it, still needing to think about project structure before starting, and still listing patterns in a log without being able to point to their structural contribution to your code — means you practiced the motions of building without acquiring the capability.

Time spent is not proof of completion. Working artifacts that meet the criteria above are.

# PATTERN QUICK REFERENCE

| Pattern | Week | Where It Lives in Flet | What It Solves |
|---|---:|---|---|
| Singleton | 1 | state/app_state.py | One source of truth for app-wide state |
| Prototype | 1 | views/screen_base.py | Clone base screen config instead of rebuilding |
| Factory | 1 | views/screen_factory.py | Single entry point for creating configured views |
| Facade | 2 | components/ (entire folder) | Clean interface over raw Flet control complexity |
| Decorator | 2 | components/decorators.py | Add loading/error behavior without subclassing |
| Composite | 2 | Every screen file | Screens as trees of components, not flat control lists |
| Observer | 3 | state/store.py | UI reacts to state changes without direct coupling |
| Command | 3 | commands/ | User actions as objects, not inline callbacks |
| Strategy | 3 | data/strategies.py | Swap mock vs. live data without changing views |
| Memento | 3 | persistence/snapshot.py | Local persistence as a serialized state snapshot |
| Template Method | 4 | views/base_screen.py | Define screen lifecycle once, override per screen |
| MVC | 4 | models/ views/ controllers/ | Explicit separation enforced by folder structure |
| Mediator | 4 | state/tab_mediator.py | Tab communication through one central object |
