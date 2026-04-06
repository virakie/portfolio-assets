import os
from collections import defaultdict

repo_path = r"E:\Virak\Portfolio Site\portfolio-assets"
github_user = "virakie"
repo_name = "portfolio-assets"
branch = "main"

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

# Build markdown output
lines = []
lines.append("# Portfolio Assets\n")

for project in sorted(projects.keys()):
    lines.append(f"## {project.replace('-', ' ').title()}\n")
    lines.append("```")
    for rel_path, url in sorted(projects[project]):
        filename = rel_path.split("/")[-1]
        lines.append(f"{filename}")
        lines.append(f"{url}")
        lines.append("")
    lines.append("```")
    lines.append("")

markdown = "\n".join(lines)

# Print to console
print(markdown)

# Also save to a .md file next to this script
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portfolio-urls.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"\n--- Saved to {output_path} ---")
input("\nPress Enter to close...")