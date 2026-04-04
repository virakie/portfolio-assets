import os
import subprocess

# CONFIG
repo_path = r"E:\Virak\Portfolio Site\portfolio-assets"
github_user = "virakie"
repo_name = "portfolio-assets"
branch = "main"

os.chdir(repo_path)
result1 = subprocess.run(["git", "add", "."], capture_output=True, text=True)
print("GIT ADD:", result1.stdout, result1.stderr)

result2 = subprocess.run(["git", "commit", "-m", "Add video assets"], capture_output=True, text=True)
print("GIT COMMIT:", result2.stdout, result2.stderr)

result3 = subprocess.run(["git", "push", "origin", branch], capture_output=True, text=True)
print("GIT PUSH:", result3.stdout, result3.stderr)

print("\n--- jsDelivr URLs ---\n")
for root, dirs, files in os.walk(repo_path):
    dirs[:] = [d for d in dirs if d != ".git"]
    for file in files:
        if file.endswith((".mp4", ".webm")):
            rel_path = os.path.relpath(os.path.join(root, file), repo_path)
            rel_path = rel_path.replace("\\", "/")
            url = f"https://cdn.jsdelivr.net/gh/{github_user}/{repo_name}@{branch}/{rel_path}"
            print(f"{rel_path}:\n{url}\n")

input("\nPress Enter to close...")