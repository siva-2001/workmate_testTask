import argparse
from router import router


def getArgs():
    parseObj = argparse.ArgumentParser(description="Arg parser for Workmate TestTask",)
    parseObj.add_argument("-r", "--report", type=str, help="type of report", default="average")
    parseObj.add_argument("-f", "--files", type=str, nargs="*", help="type of report")
    parseObj.add_argument("-d", "--dates", type=str, nargs="*", help="dates of report")
    return parseObj.parse_args()


if __name__ == "__main__":
    args = getArgs().__dict__
    reportType = args.pop("report")
    handler = router.get_method(reportType)
    if(handler): handler(**args)
