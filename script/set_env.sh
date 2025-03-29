#!/bin/bash

# Dynamically determine the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Export repository root
export REPO_ROOT
echo "Repository Root: $REPO_ROOT"

# Create and navigate to the build directory
export BUILD_DIR="$REPO_ROOT/build"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"
echo "Build Directory: $BUILD_DIR"

# Enable colored output for GCC and Clang
export GCC_COLORS=1
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

# Set up aliases
alias cmake_configure="cmake -S \"$REPO_ROOT\" -B \"$BUILD_DIR\" -G \"Unix Makefiles\""
alias cmake_build="cmake --build \"$BUILD_DIR\" -- -j$(nproc)"
alias cmake_clean="rm -rf \"$BUILD_DIR\"/* \"$BUILD_DIR\"/.* 2>/dev/null || true && echo 'Build directory cleaned.'"

# Alias for debugging
alias gdb="gdb -q" # Quiet mode

# Print success message
echo "Environment set up!"
echo "Run 'cmake_configure' to configure the project."
echo "Run 'cmake_build' to build with parallel jobs."