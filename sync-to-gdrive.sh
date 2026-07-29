#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

SOURCE_DIR="${SOURCE_DIR:-$HOME/KnowledgeHub}"
REMOTE_NAME="${REMOTE_NAME:-mymac}"
REMOTE_PATH="${REMOTE_PATH:-Knowledge Hub}"
LOG_DIR="${LOG_DIR:-$SCRIPT_DIR/rclone-logs}"
EXCLUDE_FILE="${EXCLUDE_FILE:-$SCRIPT_DIR/rclone-vault-excludes.txt}"

RUN_MODE="${1:---dry-run}"
if [[ "$RUN_MODE" != "--dry-run" && "$RUN_MODE" != "--run" ]]; then
  echo "Usage: $0 [--dry-run|--run]"
  echo
  echo "Environment overrides:"
  echo "  SOURCE_DIR=/path/to/local/folder"
  echo "  REMOTE_NAME=mymac"
  echo "  REMOTE_PATH='Knowledge Hub'"
  echo "  LOG_DIR=/path/to/logs"
  echo "  EXCLUDE_FILE=/path/to/rclone-vault-excludes.txt"
  exit 2
fi

if ! command -v rclone >/dev/null 2>&1; then
  echo "Error: rclone is not installed or not on PATH."
  exit 1
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Error: source folder does not exist: $SOURCE_DIR"
  exit 1
fi

mkdir -p "$LOG_DIR"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
LOG_FILE="$LOG_DIR/rclone-sync-$TIMESTAMP.log"
DESTINATION="${REMOTE_NAME}:${REMOTE_PATH}"

echo "Source:      $SOURCE_DIR"
echo "Destination: $DESTINATION"
echo "Log file:    $LOG_FILE"

RCLONE_ARGS=(
  sync
  "$SOURCE_DIR"
  "$DESTINATION"
  --progress
  --create-empty-src-dirs
  --exclude-from "$EXCLUDE_FILE"
  --log-file "$LOG_FILE"
  --log-level INFO
)

if [[ "$RUN_MODE" == "--dry-run" ]]; then
  echo "Mode:        dry-run, no files will be changed"
  RCLONE_ARGS+=(--dry-run)
else
  echo "Mode:        real sync"
fi

rclone "${RCLONE_ARGS[@]}"
