import requests

url = "https://api.github.com/users/lapeko/repos"

response = requests.get(url)
repos = response.json()

for repo in repos:
    print(repo["name"])
    print(repo["html_url"])
