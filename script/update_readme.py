import os
import json
import subprocess
import sys
from dataclasses import dataclass

try:
    import requests
except ImportError:
    print("Installing missing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

@dataclass
class LeetCodeProblem:
    title: str
    difficulty: str
    category: str
    link: str

# Environment variable REPO_ROOT should be set to the root of the repository
# This is typically done by sourcing the setup_env.sh script
REPO_ROOT = os.getenv("REPO_ROOT")
if not REPO_ROOT:
    raise EnvironmentError("REPO_ROOT environment variable is not set. Please source setup_env.sh.")

README_PATH = os.path.join(REPO_ROOT, "README.md")
SRC_DIR = os.path.join(REPO_ROOT, "src")

def fetch_problem_data(slug: str):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                title
                difficulty
                categoryTitle
            }
        }
        """,
        "variables": {"titleSlug": slug}
    }
    
    try:
        response = requests.post(url, headers=headers, json=query, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_problem_data(data, slug: str):
    """
    Fetch the LeetCode problem details using the titleSlug.
    """
    if not data or "data" not in data or not data["data"].get("question"):
        print(f"Invalid or missing data for slug: {slug}")
        return None
    
    question = data["data"]["question"]
    return LeetCodeProblem(
        title=question["title"],
        difficulty=question["difficulty"],
        category=question.get("categoryTitle", "Unknown"),
        link=f"https://leetcode.com/problems/{slug}/"
    )

def color_difficulty(difficulty: str) -> str:
    """
    Add color to the difficulty level.
    """
    if difficulty == "Easy":
        return f'<span style="color: green;">{difficulty}</span>'
    elif difficulty == "Medium":
        return f'<span style="color: orange;">{difficulty}</span>'
    elif difficulty == "Hard":
        return f'<span style="color: red;">{difficulty}</span>'
    else:
        return difficulty  # Default black for "Invalid" or unknown

def generate_table_rows():
    table_rows = []

    for problem in sorted(os.listdir(SRC_DIR)):
        problem_path = os.path.join(SRC_DIR, problem)
        if os.path.isdir(problem_path):
            slug = problem  # Assuming the directory name matches the titleSlug
            data = fetch_problem_data(slug)
            details = parse_problem_data(data, slug)
            if details:
                table_rows.append(
                    f"| [{details.title}](src/{slug}/) | [{details.link}]({details.link}) | {color_difficulty(details.difficulty)} | {details.category} |\n"
                )
            else:
                table_rows.append(
                    f"| {slug} | N/A | N/A | N/A |\n"
                )

    return table_rows

def update_readme():
    with open(README_PATH, "r") as file:
        lines = file.readlines()

    # Locate "# Problems Solved" section
    start_index = None
    for i, line in enumerate(lines):
        if line.strip() == "# Problems Solved":
            start_index = i + 2  # Skip the header line
            break

    if start_index is None:
        print("Error: Could not find '# Problems Solved' section in README.md")
        return

    # Generate the new table rows (without the header)
    table_rows = generate_table_rows()

    # Replace the old table with the new one
    end_index = start_index
    while end_index < len(lines) and lines[end_index].strip().startswith("|"):
        end_index += 1

    # Add the header and rows
    table_header = "| Title                | LeetCode Link                       | Difficulty       | Category       |\n"
    table_header += "|---------------------|-------------------------------------|------------------|----------------|\n"
    updated_lines = lines[:start_index] + [table_header] + table_rows + lines[end_index:]

    with open(README_PATH, "w") as file:
        file.writelines(updated_lines)

    print("README.md updated successfully!")

if __name__ == "__main__":
    update_readme()