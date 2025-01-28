from src.argv import Argparser
from src import check, check_login, issue, upload

args = Argparser().args

token: str = args.token


if args.check_login:
    check_login.run(args.ali)
elif args.check:
    check.run(token)
elif args.upload:
    UP = upload.Upload()
    UP.ali(args.ali, 1)
    UP.baidu()
elif args.issue:
    issue.run(token)
