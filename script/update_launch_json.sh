#!/bin/bash
BIN_DIR="$REPO_ROOT/build/bin"
LAUNCH_JSON="$REPO_ROOT/.vscode/launch.json"

# Extract binary names
BINARIES=$(ls "$BIN_DIR" 2>/dev/null)

# Check if BINARIES is empty
if [ -z "$BINARIES" ]; then
  OPTIONS="[]"
else
  # Generate JSON options
  OPTIONS=$(printf '"%s",' $BINARIES)
  OPTIONS="[${OPTIONS%,}]" # Remove trailing comma and wrap in brackets
fi

# Update launch.json
jq --argjson options "$OPTIONS" \
   '.inputs[0].options = $options' "$LAUNCH_JSON" > temp.json && mv temp.json "$LAUNCH_JSON"