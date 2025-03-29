# C++ LeetCode Debugging Environment

This repository provides a robust C++ environment for efficiently solving and debugging LeetCode problems.

## Requirements

### Operating System
- Linux (tested on Ubuntu-based distributions)

### Libraries and Tools
- **C++ Compiler**: GCC (g++) 11 or later
- **Build System**: CMake 3.10 or later
- **Debugger**: gdb
- **Version Control**: Git
- **Editor/IDE**: Visual Studio Code (recommended) with the following extensions:
  - C/C++ (Microsoft)
  - CMake Tools
  - GitLens

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd CppLeetCodeEnv
   source script/set_env.sh
   ```

2. **Install Essential Tools**:
   Ensure that all required tools and libraries are installed on your system. For example:
   ```bash
   sudo apt update
   sudo apt install build-essential cmake gdb git jq
   ```

3. **Add a Problem to Debug**:
   Place your LeetCode problem's source file in the `src/<LeetCodeProblemTitle>/` directory. For example:
   ```bash
   ./src/<LeetCodeProblemTitle>/main.cpp
   ```
   You may also include additional dependency files in the problem's directory. These files will be built together.

4. **Build the Problem**:
   Build your problem within the `./build` directory:
   ```bash
   cmake_configure && cmake_build
   ```

5. **Update VSCode Debug Configuration**:
   Update the `launch.json` file for debugging by running:
   ```bash
   bash script/update_launch_json.sh
   ```

6. **Launch the Debugger**:
   Open Visual Studio Code, press `F5`, and start debugging your problem.
