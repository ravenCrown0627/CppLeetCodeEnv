import os

REPO_ROOT = os.getenv("REPO_ROOT")
if not REPO_ROOT:
    raise EnvironmentError("REPO_ROOT environment variable is not set. Please source set_env.sh.")

README_PATH = os.path.join(REPO_ROOT, "README.md")
SRC_DIR = os.path.join(REPO_ROOT, "src")

def generate_table():
    table_header = "| Problem Title       | Path                                   |\n"
    table_header += "|---------------------|----------------------------------------|\n"
    table_rows = []

    for problem in sorted(os.listdir(SRC_DIR)):
        problem_path = os.path.join(SRC_DIR, problem)
        if os.path.isdir(problem_path):
            table_rows.append(f"| {problem} | [src/{problem}/](src/{problem}/) |\n")

    return table_header + "".join(table_rows)

def update_readme():
    with open(README_PATH, "r") as file:
        lines = file.readlines()

    # Find where to insert the table
    start_index = None
    for i, line in enumerate(lines):
        if line.strip() == "# Solved Problems":
            start_index = i + 2  # Skip the header line
            break

    if start_index is None:
        print("Error: Could not find '# Solved Problems' section in README.md")
        return

    # Generate the new table
    table = generate_table()

    # Replace the old table with the new one
    end_index = start_index
    while end_index < len(lines) and lines[end_index].strip().startswith("|"):
        end_index += 1

    updated_lines = lines[:start_index] + [table] + lines[end_index:]

    with open(README_PATH, "w") as file:
        file.writelines(updated_lines)

if __name__ == "__main__":
    update_readme()