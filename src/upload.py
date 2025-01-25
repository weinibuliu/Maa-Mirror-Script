from pathlib import Path

import aligo
import bypy

from .config.ALI import ALI

REL_PATH = Path.cwd()


class Upload:
    def __init__(self):

        self.releases = [
            f for f in REL_PATH.glob("*") if "zip" in str(f) or ".exe" in str(f)
        ]
        self.platforms = ["win-x64"]

        if not self.releases:
            raise RuntimeError(f"{REL_PATH} is empty.")

    def ali(self, token: str, config_num: int):
        platforms = self.platforms

        config = ALI[config_num]
        DRIVE_ID = config["DRIVE_ID"]
        DIR_ID = config["DIR_ID"]

        file_ids = []

        ali = aligo.Aligo(refresh_token=token)

        for pla in platforms:
            for r in self.releases:
                if "Debug" in str(r):
                    continue
                if pla in str(r):
                    name = r.name
                    if pla == "win-x64":
                        if ".exe" not in str(r):
                            continue
                        name = name.replace(".exe", ".7z")
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
        else:
            print(file_ids)

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
