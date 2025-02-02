from src.argv import Argparser
from src import check, check_login, issue, upload

args = Argparser().args

token: str = args.token


if args.check_login:
    check_login.run(args.ali)
elif args.check:
    check.MAA(token).run()
elif args.check_res:
    check.Resource(token).run()
elif args.upload:
    UP = upload.Upload(args.ali)
    UP.ali()
    UP.baidu()
elif args.upload_res:
    UP = upload.Res_Upload(args.ali)
    UP.ali()
    UP.baidu()
elif args.issue:
    issue.Issue(token).run()
elif args.issue_res:
    issue.Issue(token).update_res()
