#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="koko-seo-geo-llmo-aeo"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
SKILLS_DIR="$CODEX_HOME/skills"
TARGET_LINK="$SKILLS_DIR/$SKILL_NAME"

mkdir -p "$SKILLS_DIR"

if [ -L "$TARGET_LINK" ]; then
  rm "$TARGET_LINK"
elif [ -e "$TARGET_LINK" ]; then
  echo "A path already exists at $TARGET_LINK and is not a symlink."
  echo "Move or remove it, then run this installer again."
  exit 1
fi

ln -s "$REPO_DIR" "$TARGET_LINK"

cat <<EOF
Installed $SKILL_NAME into:
  $TARGET_LINK

Next step:
  Restart Codex to load the new skill.
EOF
