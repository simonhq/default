import asyncio
import json
import os
from glob import glob

from aiogithubapi import GitHub
from scripts.changed.repo import get_repo

TOKEN = os.getenv("GITHUB_TOKEN")


async def check():
    repo = get_repo()
    issues = []
    async with GitHub(TOKEN) as github:
        repository = await github.get_repo(repo)
        repo = repository.attributes


    if not repo["has_issues"]:
        issues.append("Issues not enabled.")

    if not repo["description"]:
        issues.append("No description. (https://hacs.xyz/docs/publish/start#description)")

    if not repo["topics"]:
        issues.append("No topics. (https://hacs.xyz/docs/publish/start#topics)")

    if issues:
        for issue in issues:
            print(issue)
        exit(1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(check())
