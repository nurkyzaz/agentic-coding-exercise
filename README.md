# ILIAD Intensive C.1.3 — OpenCode exercises

Hands-on exercises for learning to work with OpenCode on a small ML research
codebase. The running project is a steganography study: can a model secretly
transmit numbers inside an ordinary answer, and can a monitor catch it?

## Install OpenCode

- **macOS / Linux**: `curl -fsSL https://opencode.ai/install | bash` (or `brew install sst/tap/opencode`)
- **Windows**: `npm i -g opencode-ai`, plus [Git for Windows](https://git-scm.com/downloads/win)
  for a Bash shell (the course assumes Bash).

Then `cd` to your project and run `opencode`. To connect a model, run `/connect` inside
OpenCode (or `opencode auth login`), pick a provider and paste your key. If you use the
course API key: it is shared, so use it only for the course project work and never post it
anywhere public. [Docs](https://opencode.ai/docs/)

### Optional: herdr (macOS / Linux)

[herdr](https://herdr.dev/) is a terminal workspace manager built for running several
coding agents at once (one workspace per project, one tab per branch), and it shows which
agent needs you. Install it with:

```bash
curl -fsSL https://herdr.dev/install.sh | sh
```

then run `herdr`. To look at files next to OpenCode, install [neovim](https://neovim.io/)
(`brew install neovim` on macOS; on Linux use the [release binaries](https://github.com/neovim/neovim/blob/master/INSTALL.md),
apt's version is too old) with [LazyVim](https://www.lazyvim.org/installation).
Plain neovim already takes mouse clicks and scrolling; LazyVim adds a file tree and tabs you
can click.

For a ready-made setup (herdr, keybindings, neovim, Claude settings), see
the minimal version of my dotfiles: [wusche1/dotfiles @ minimal](https://github.com/wusche1/dotfiles/tree/minimal).

### Cheat sheets

- OpenCode: https://opencode.ai/docs/
- herdr: https://cskwork.github.io/herdr-cheatsheet/

## Exercises

Each exercise is a branch and adds one technique: the basic ask → edit → run → read-the-diff
loop (00), plan mode (01), subagents (02), worktrees and the Ralph loop (03).

| Branch | Topic |
|---|---|
| `exercise-0` | One script — ask, edit, run, read the diff |
| `exercise-1` | Logging & config — plan mode |
| `exercise-2` | Monitor & schemes — subagents |
| `exercise-3` | Best scheme & self-invented schemes — worktrees + `/ralph-loop` |

Check one out and read its `EXERCISE.md`:

```bash
git checkout exercise-1
```

Setup: [uv](https://docs.astral.sh/uv/) manages deps, and runs need an
`OPEN_ROUTER_API_KEY` in `.env` (loaded automatically by python-dotenv).

```bash
uv sync
cd experiments/<name>
uv run python main.py -c configs/<config>.yaml
```

See `AGENTS.md` for the repo conventions.
