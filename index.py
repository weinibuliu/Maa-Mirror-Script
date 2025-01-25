from src.argv import Argparser
from src import check, issue, upload

args = Argparser().args

token: str = args.token

if args.check:
    check.run(token)
elif args.upload:
    UP = upload.Upload()
    UP.ali(args.ali, 1)
    UP.baidu()
elif args.issue:
    issue.run(token)
