#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="koko-seo-geo-llmo-aeo"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
TARGET_LINK="$CODEX_HOME/skills/$SKILL_NAME"

if [ -L "$TARGET_LINK" ]; then
  rm "$TARGET_LINK"
  echo "Removed symlink: $TARGET_LINK"
  exit 0
fi

if [ -e "$TARGET_LINK" ]; then
  echo "Found a non-symlink path at $TARGET_LINK."
  echo "Not removing it automatically."
  exit 1
fi

echo "Nothing to remove. $TARGET_LINK was not found."
