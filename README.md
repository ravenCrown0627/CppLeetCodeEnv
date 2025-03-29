# C++ LeetCode Debugging Environment

This repository provides a robust C++ environment for efficiently solving and debugging LeetCode problems.

# Problems Solved

| Title                | LeetCode Link                       | Difficulty       | Category       |
|---------------------|-------------------------------------|------------------|----------------|
| [Two Sum](src/two-sum/) | [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/) | <span style="color: green;">Easy</span> | Algorithms |

# Requirements

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

# Automate README Problem List Update (Optional)
To automatically update the problem list in the `README.md` file after every commit, you can set up a `post-commit` Git hook. Follow these steps:

1. **Create the `post-commit` Hook**:
   Navigate to the `.git/hooks` directory and create a file named `post-commit`:
   ```bash
   touch .git/hooks/post-commit
   ```
2. **Add the Following Script to post-commit**: 
    Copy and paste the following script into the post-commit file:
    ```bash
    #!/bin/bash
    
    # Source the set_env.sh script to load environment variables
    source "$(dirname "${BASH_SOURCE[0]}")/../../script/set_env.sh"
    
    # Call the script to update the README using the SCRIPT_DIR variable
    python3 "$SCRIPT_DIR/update_readme.py"
    # Check if the README was updated successfully
    if [ $? -ne 0 ]; then
        echo "Failed to update README."
        exit 1
    fi
    # Add the updated README to the latest commit
    git add README.md
    git commit --amend --no-edit
    # Check if the commit was successful
    if [ $? -ne 0 ]; then
        echo "Failed to amend the commit."
        exit 1
    fi
    # Display the commit message
    echo "Commit amended successfully. Here is the commit message:"
    git log -1 --pretty=format:"%h %s"
    
    # Display the updated README content
    echo "README has been updated. Here is the updated content:"
    cat README.md
    ```
3. **Make the Hook Executable**: 
    Run the following command to make the post-commit script executable:
    ```bash
    chmod +x .git/hooks/post-commit
    ```
4. **Verify the Hook**: 
    After making a commit, the post-commit hook will automatically update the `README.md` file and amend the commit to include the changes.
    > **❗Note:** Ensure that the `script/update_readme.py` script exists and is functional. This script is responsible for updating the problem list in the `README.md` file.