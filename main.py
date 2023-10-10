# minitest -c config.json -s suite.json -g
#"D:\software\微信web开发者工具\cli.bat" auto --project "D:\software\mini-data\c-luluyou\unpackage\dist\dev\mp-weixin" --auto-port 9421

import os
import pytest


pytest.main(["tests", "-sv", "--alluredir", "./report/temp_jsonreport"])
os.system("allure generate ./report/temp_jsonreport -o ./report/html --clean")
