from pathlib import Path

import aligo
import bypy

from .config.ALI import ALI

REL_PATH = Path.cwd()


class Upload:
    def __init__(self, ali_token: str, config_num: int = 1):
        self.ali_token = ali_token
        self.config_num = config_num
        self.releases = [
            f for f in REL_PATH.glob("*") if "zip" in str(f) or ".7z" in str(f)
        ]
        self.platforms = ["win-x64"]

        if not self.releases:
            raise RuntimeError(f"{REL_PATH} is empty.")

    def ali(self):
        platforms = self.platforms

        config = ALI[self.config_num]
        DRIVE_ID = config["DRIVE_ID"]
        DIR_ID = config["DIR_ID"]

        file_ids = []

        ali = aligo.Aligo(
            refresh_token=self.ali_token,
            requests_timeout=5,
            re_login=False,
        )

        for pla in platforms:
            for r in self.releases:
                if "Debug" in str(r):
                    continue
                if pla in str(r):
                    name = r.name
                    if pla == "win-x64":
                        if ".7z" not in str(r):
                            continue
                    file = ali.upload_file(
                        r, DIR_ID[pla], name, DRIVE_ID, check_name_mode="overwrite"
                    )
                    file_id = file.file_id
                    status = file.status
                    if not file_id:
                        raise RuntimeError(f"Fail to upload {pla} ({status})")
                    file_ids.append({pla: file_id})
                    break
        if not file_ids:
            raise RuntimeError(f"Fail to upload.")

    def baidu(self):
        platforms = self.platforms
        remote_path = "Maa Mirror"

        by = bypy.ByPy(verify=False)

        for pla in platforms:
            for r in self.releases:
                if "Debug" in str(r):
                    continue
                if pla in str(r):
                    if pla == "win-x64":
                        if ".zip" not in str(r):
                            continue
                    by.upload(str(r), f"{remote_path}/{pla}/{r.name}")


class Res_Upload:
    def __init__(self, ali_token: str, config_num: int = 1):
        self.ali_token = ali_token
        self.config_num = config_num

        self.res_path = Path(Path.cwd(), "Resource.zip")
        self.res_7z_path = Path(Path.cwd(), "Resource.7z")

        for p in [self.res_path, self.res_7z_path]:
            if not p.exists():
                raise FileNotFoundError(f"{p} dose not exist.")

    def ali(self):
        config = ALI[self.config_num]
        DRIVE_ID = config["DRIVE_ID"]
        DIR_ID = config["DIR_ID"]["root"]

        ali = aligo.Aligo(
            refresh_token=self.ali_token,
            requests_timeout=5,
            re_login=False,
        )
        file = ali.upload_file(
            str(self.res_7z_path),
            DIR_ID,
            drive_id=DRIVE_ID,
            check_name_mode="overwrite",
        )

        if not file.file_id:
            raise RuntimeError("Fail to upload Resource.")

    def baidu(self):
        remote_path = "Maa Mirror"

        by = bypy.ByPy(verify=False)
        by.upload(str(self.res_path), f"{remote_path}/Resource.zip")
