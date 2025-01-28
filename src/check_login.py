import logging
import os

import aligo
import bypy


def ali(token: str | None = None) -> bool:
    try:
        a = aligo.Aligo(
            refresh_token=token,
            requests_timeout=5,
            re_login=False,
            level=logging.CRITICAL + 1,
        )
        a.get_default_drive()
    except:
        return False
    return True


def baidu() -> bool:
    try:
        by = bypy.ByPy()
        by.info()
    except:
        return False
    return True


def run(ali_token: str | None = None):
    print("Start: Check Login Status")

    ali_status = ali(ali_token)
    baidu_status = baidu()

    if ali_status and baidu_status:
        print("Login Status is all right")
    else:
        print(f"ALi Pan: {ali_status}")
        print(f"BaiDu Pan: {baidu_status}")
        print("\nToken Error,please check outputs.")
        exit(1)  # 非0退出码会导致 Github Action 异常
