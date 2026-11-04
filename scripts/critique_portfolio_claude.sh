#!/usr/bin/env bash
set -euo pipefail

critic_script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$critic_script_dir/.."

# Uses Claude's existing login. Only file-reading tools are available.
exec claude --print --restricted --strict-mcp-config \
  --permission-mode plan --permission-prompts none \
  --tools 'Read,Glob,Grep' --allowedTools 'Read,Glob,Grep' \
  --no-session-persistence --no-chrome --output-format text \
  < "$critic_script_dir/claude_portfolio_critic.txt"
