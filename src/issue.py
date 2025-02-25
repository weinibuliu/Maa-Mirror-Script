import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import github

from .ISSUE_BODY import BODY, RESOURCE

VERSION_PATH = Path(Path.cwd(), "version")
VERSION_RES_PATH = Path(Path.cwd(), "version.json")
RELEASE_TIME_PATH = Path(Path.cwd(), "release_time")
NOTE_PATH = Path(Path.cwd(), "note.md")
NOTICE_URL = "https://mmirror.top/post/gong-gao.html"
DOWNLOAD_URL = "https://mmirror.top/download.html"
RES_ISSUE_ID = 27  # https://github.com/MaaMirror/Maa-Mirror/issues/27


class Issue:
    def __init__(self, token: str):
        GH = github.Github(login_or_token=token, retry=None)
        self.REPO = GH.get_repo("MaaMirror/Maa-Mirror")

    def test(self):
        self.REPO.create_issue("Test", "This is a test for token.", labels=["update"])

    def run(self):
        tz = timezone(timedelta(hours=8))
        _time = datetime.now().timestamp()
        time = datetime.fromtimestamp(int(_time)).astimezone(tz)

        with open(VERSION_PATH, "r", encoding="utf-8") as f:
            ver = f.read()
        with open(RELEASE_TIME_PATH, "r", encoding="utf-8") as f:
            ts = int(f.read())
            release_time = datetime.fromtimestamp(ts, tz)
        with open(NOTE_PATH, "r", encoding="utf-8") as f:
            note = f.read()

        labels = ["update"]
        if "beta" in ver or "alpha" in ver:
            labels.append("unstable")
        else:
            labels.append("stable")

        title = ver
        body = BODY.replace("{VERSION}", ver).replace("{NOTE}", note)
        body = body.replace("{NOTICE_URL}", NOTICE_URL)
        body = body.replace("{DOWNLOAD_URL}", DOWNLOAD_URL)
        body = body.replace("{TIME}", str(time))
        body = body.replace("{RELEASE_TIME}", str(release_time))
        self.REPO.create_issue(title=title, body=body, labels=labels)

    def update_res(self):
        tz = timezone(timedelta(hours=8))
        _time = datetime.now().timestamp()
        update_time = datetime.fromtimestamp(int(_time), tz)

        with open(VERSION_RES_PATH, "r", encoding="utf-8") as f:
            cache = json.load(f)
            res_ver = cache["activity"]["name"]
            time = cache["last_updated"]

            time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f").astimezone(tz)

        body = RESOURCE.replace("{RES_VER}", res_ver)
        body = body.replace(
            "{RES_TIME}", str(time).split("+")[0][:-3] + "+08:00"
        )  # 切片，保留微秒前三位
        body = body.replace("{NOTICE_URL}", NOTICE_URL)
        body = body.replace("{DOWNLOAD_URL}", DOWNLOAD_URL)
        body = body.replace("{TIME}", str(update_time))

        self.REPO.get_issue(RES_ISSUE_ID).edit(body=body)
