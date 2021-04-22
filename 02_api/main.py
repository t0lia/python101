import json
import sys

import requests


def main():
    api_token = load_token()
    headers = {"Authorization": f"token {api_token}"}

    username = sys.argv[1]
    print(f"get info for {username}...")
    validate_user(headers, username)

    save_repo_info(headers, username)
    result = {}
    with open("results/github.json", "r") as read_file:
        info = json.load(read_file)
        for repo in info:
            for language in info[repo]:
                if language in result:
                    result[language] += 1
                else:
                    result[language] = 1
    for k in sorted(result, key=result.get, reverse=True):
        print(k, result[k])


def save_repo_info(headers, username):
    repos = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers).json()
    rate = {}
    for repo in repos:
        language_response = requests.get(repo["languages_url"], headers=headers).json()
        languages = list(language_response.keys())
        if len(languages) > 0:
            rate[repo["name"]] = list(language_response.keys())
    with open("results/github.json", "w") as gh_file:
        json.dump(rate, gh_file, indent=2)


def validate_user(headers, username):
    user_response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    if user_response.status_code != 200:
        print(f"problem with api access, response code: {user_response.status_code}", file=sys.stderr)
        exit(1)


def load_token():
    with open("secret/configuration.json", "r") as read_file:
        configuration = json.load(read_file)
    api_token = configuration["token"]
    return api_token


if __name__ == "__main__":
    main()
