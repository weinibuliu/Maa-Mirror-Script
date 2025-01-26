from datetime import datetime
from pathlib import Path

import github

from .ISSUE_BODY import BODY

VERSION_PATH = Path(Path.cwd(), "version")
NOTE_PATH = Path(Path.cwd(), "note.md")
NOTICE_URL = "https://mmirror.top/post/1.html"
DOWNLOAD_URL = "https://mmirror.top/download.html"


def run(token: str | None = None):
    with open(VERSION_PATH, "r", encoding="utf-8") as f:
        ver = f.read()
    with open(NOTE_PATH, "r", encoding="utf-8") as f:
        note = f.read()

    GH = github.Github(login_or_token=token, retry=None)
    REPO = GH.get_repo("weinibuliu/Maa-Mirror")

    labels = ["maa", "update"]
    if "beta" in ver or "alpha" in ver:
        labels.append("unstable")
    else:
        labels.append("stable")

    title = ver
    body = BODY.replace("{VERSION}", ver).replace("{NOTE}", note).replace("@", "By ")
    body = body.replace("{NOTICE_URL}", NOTICE_URL).replace(
        "{DOWNLOAD_URL}", DOWNLOAD_URL
    )
    body = body.replace("{TIME}", str(datetime.now()))
    REPO.create_issue(title=title, body=body, labels=labels)
