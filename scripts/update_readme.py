import requests
import os

USERNAME = "Selbstlader"
API_URL = f"https://api.github.com/users/{USERNAME}/repos"
README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")

response = requests.get(API_URL)
repos = response.json()

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(f"# {USERNAME} 的仓库列表\n\n")
    for repo in repos:
        f.write(f"- [{repo['name']}]({repo['html_url']})\n") 