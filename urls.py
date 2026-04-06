import os
import subprocess
import pyperclip
from collections import defaultdict

# CONFIG
repo_path = r"E:\Virak\Portfolio Site\portfolio-assets"
github_user = "virakie"
repo_name = "portfolio-assets"
branch = "main"

# --- GIT PUSH ---
os.chdir(repo_path)

result1 = subprocess.run(["git", "add", "."], capture_output=True, text=True)
print("GIT ADD:", result1.stdout, result1.stderr)

result2 = subprocess.run(["git", "commit", "-m", "Add video assets"], capture_output=True, text=True)
print("GIT COMMIT:", result2.stdout, result2.stderr)

print("GIT PUSH: uploading...")
subprocess.run(["git", "push", "origin", branch])

# --- BUILD URLS ---
projects = defaultdict(list)

for root, dirs, files in os.walk(repo_path):
    dirs[:] = [d for d in dirs if d != ".git"]
    for file in files:
        if file.endswith((".mp4", ".webm")):
            rel_path = os.path.relpath(os.path.join(root, file), repo_path)
            rel_path = rel_path.replace("\\", "/")
            parts = rel_path.split("/")
            project = parts[0]
            url = f"https://cdn.jsdelivr.net/gh/{github_user}/{repo_name}@{branch}/{rel_path}"
            projects[project].append((rel_path, url))

# --- BUILD MARKDOWN (preserving original folder name casing) ---
lines = []
lines.append("# Portfolio Assets\n")

for project in sorted(projects.keys()):
    lines.append(f"## {project}\n")
    lines.append("```")
    for rel_path, url in sorted(projects[project]):
        filename = rel_path.split("/")[-1]
        lines.append(filename)
        lines.append(url)
        lines.append("")
    lines.append("```")
    lines.append("")

markdown = "\n".join(lines)

# --- COPY TO CLIPBOARD ---
pyperclip.copy(markdown)
print("\n--- Copied to clipboard ---")
print(markdown)

input("\nPress Enter to close...")