import os
import subprocess

# CONFIG
repo_path = r"E:\Virak\Portfolio Site\portfolio-assets"
github_user = "virakie"
repo_name = "portfolio-assets"
branch = "main"

os.chdir(repo_path)
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Add video assets"])
subprocess.run(["git", "push", "origin", branch])

print("\n--- jsDelivr URLs ---\n")
for root, dirs, files in os.walk(repo_path):
    dirs[:] = [d for d in dirs if d != ".git"]
    for file in files:
        if file.endswith((".mp4", ".webm")):
            rel_path = os.path.relpath(os.path.join(root, file), repo_path)
            rel_path = rel_path.replace("\\", "/")
            url = f"https://cdn.jsdelivr.net/gh/{github_user}/{repo_name}@{branch}/{rel_path}"
            print(f"{rel_path}:\n{url}\n")