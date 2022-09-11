import CLI
import os
import sys

config = CLI.cli()
try:
    config["fileName"] = sys.argv[1]
except:
    config["fileName"] = "twest.uwu"

ast = CLI.parseFile(config["fileName"], config["clearExceptions"])

os.system("pyinstaller --onefile out.py")
os.system("\"dist\\out.exe\"")