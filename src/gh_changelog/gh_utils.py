import requests
from typing import Any
from gh_changelog.core import Version
from gh_changelog.version_str_utils import parse_version_str

GITHUB_API_URL = "https://api.github.com/graphql"
TOKEN = ""


def run_query(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    response = requests.post(
        GITHUB_API_URL,
        json={"query": query, "variables": variables},
        headers={"Authorization": f"Bearer {TOKEN}"},
        timeout=10,
    )
    return response.json()


def get_tags(owner: str, repo_name: str) -> list[Version]:
    gql_get_tags: str = """query getTags($owner: String!, $name: String!) {
    repository(owner: $owner, name: $name) {
        refs(refPrefix: "refs/tags/", first: 100, orderBy: {field: TAG_COMMIT_DATE, direction: DESC}) {
        nodes {
            name
            target {
            ... on Commit {
                oid
                committedDate
            }
            ... on Tag {
                target {
                ... on Commit {
                    oid
                    committedDate
                }
                }
            }
            }
        }
        }
    }
    }
    """

    raw_dict = run_query(gql_get_tags, {"owner": owner, "name": repo_name})
    return [
        parse_version_str(entry["name"])
        for entry in raw_dict["data"]["repository"]["refs"]["nodes"]
    ]


print(get_tags("austinyu", "ujson5"))
