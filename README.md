# Exercise 03 — Best scheme & self-invented schemes (worktrees + Ralph loop)

Part of the OpenCode exercises for the ILIAD intensive. The brief is in the markdown
file next to this one. Exercise 00 is the same steganography experiment as a single script;
here it lives in a structured repo (`experiments/`, `lib/`, a config framework).

```bash
uv sync
cd experiments/<name>
uv run python main.py -c configs/<config>.yaml
```

Needs `OPEN_ROUTER_API_KEY` in `.env` (loaded automatically). See `AGENTS.md` for conventions.

## Tools for this exercise

**Worktrees** — work on several approaches in parallel, one OpenCode per checkout:

```bash
git worktree add ../steg-a -b try-a   # new branch in a sibling folder
cd ../steg-a && opencode              # one OpenCode per worktree (e.g. one herdr tab each)
git worktree remove ../steg-a         # clean up when done
```

**Ralph loop** — OpenCode's equivalent of Claude Code's `/goal`. The
[opencode-ralph-loop](https://github.com/charfeng1/opencode-ralph-loop) plugin is enabled
in `opencode.json` and installs itself on the next start. Give it a task with a checkable
end state:

```
/ralph-loop "Run the debug config for each scheme and write a results table to tmp/results.md"
```

Whenever the agent stops, the plugin sends "continue" until the agent outputs
`<promise>DONE</promise>` (max 100 iterations). Stop it early with `/cancel-ralph`.
It needs the interactive TUI: `opencode run` exits as soon as the agent goes idle.
