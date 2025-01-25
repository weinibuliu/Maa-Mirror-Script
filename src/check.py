import subprocess
from pathlib import Path

import github
import github.GitReleaseAsset

VERSION_PATH = Path(Path.cwd(), "version")
NOTE_PATH = Path(Path.cwd(), "note.md")


def get_current_ver() -> str | None:
    if not VERSION_PATH.exists():
        return None

    with open(VERSION_PATH, "r", encoding="utf-8") as f:
        return f.read()


def check(token: str | None = None) -> str | None:
    GH = github.Github(login_or_token=token, retry=None)
    REPO = GH.get_repo("MaaAssistantArknights/MaaAssistantArknights")
    RELEASE = REPO.get_latest_release()

    curent_ver = get_current_ver()

    target_ver = RELEASE.tag_name
    note = (
        RELEASE.body.replace(f"## {target_ver}\n\n", "")
        .replace(f"## {target_ver}\n", "")
        .replace("@", " By ")
    )

    if target_ver != curent_ver:
        with open(VERSION_PATH, "w", encoding="utf-8") as f:
            f.write(target_ver)
        with open(NOTE_PATH, "w", encoding="utf-8") as f:
            f.write(note)
        return target_ver
    else:
        return None


def run(token: str | None = None):
    ver = check(token)
    if ver:
        subprocess.run('echo "update=true" >> "$GITHUB_ENV"', shell=True)
        print("env.update = true")
        subprocess.run(f'echo "update_ver={ver}" >> "$GITHUB_ENV"', shell=True)
        print(f"env.update_ver = {ver}")
