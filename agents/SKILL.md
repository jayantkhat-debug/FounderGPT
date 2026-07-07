# Skill: Create SKILL.md for agent-customization

Short description
- A reusable skill template that codifies the multi-step workflow used when debugging, implementing, or customizing agents in this workspace. Produces a clear checklist, decision points, quality gates, example prompts, and recommended next steps.

When to use
- When you want to capture and reuse a step-by-step workflow or methodology that the team follows when working with code, agents, or operational procedures in this repo.

Scope
- Workspace-scoped: saved in `agents/SKILL.md` and intended for use by contributors to this repository.

Step-by-step workflow (template)
1. Understand the problem
   - Record the expected behaviour, edge cases, and success criteria.
   - Identify constraints (time, data, access, security).

2. Investigate the codebase
   - Locate relevant files, tests, and configs.
   - Run quick searches for key symbols and read surrounding context.

3. Create a concise plan
   - Break the fix/feature into small, testable steps.
   - For each step include: goal, file(s) to change, tests to run, and rollback plan.

4. Implement incrementally
   - Make small commits per step; prefer minimal, reversible changes.
   - Run unit tests and linters locally after each change.

5. Debug and iterate
   - When tests fail, gather logs, reproduce, and narrow root cause.
   - Add targeted tests that reproduce the bug before fixing.

6. Validate and finalize
   - Ensure code style, type checks, and CI pass.
   - Write or update documentation and examples.

Decision points and branching logic
- If tests reproduce the issue: write a failing unit test and fix code.
- If no local reproduction: add instrumentation/logging and rerun in environment.
- If fix requires infra/config changes: open an RFC and get approvals before applying.

Quality criteria / completion checks
- All tests (unit/integration) pass locally.
- New behavior covered by tests and documented.
- Change is reviewed (PR) and passes CI.
- No new high-severity lint/type errors.

Ambiguities & clarifications
- If no clear workflow emerges from a conversation, use this template and ask:
  - "What is the desired outcome and success criteria?"
  - "Should this be workspace-scoped or personal?"
  - "Do we need a quick checklist or a full multi-step workflow?"

Safety & limits note
- This skill aims to be permissive and helpful, but it cannot bypass legal, ethical, or platform safety constraints. It will not assist in harmful, illegal, or policy-violating requests.

Example prompts to use this skill
- "Create a SKILL.md that codifies our debugging workflow for backend services." 
- "Draft a workspace-scoped skill that automates code review checklists for PRs." 
- "Turn our deployment runbook into a SKILL.md with decision trees and rollback steps."

Suggested customizations
- Add repository-specific file paths and common search terms.
- Include links to CI, deployment dashboards, and runbooks.
- Provide example PR templates and changelog snippets.

Iteration plan
1. Draft the SKILL.md (this file).
2. Ask maintainers for missing details and repository-specific rules.
3. Update the file with concrete file paths, commands, and examples.
4. Add small tests or CI checks that verify presence of SKILL.md or follow conventions.

Created-by: assistant
Date: 2026-07-08
