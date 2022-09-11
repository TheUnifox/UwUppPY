import Parser

cliConfig = {"fileName": "twest.uwu", "outputFile": "out.py", "clearExceptions": False}

def cli():
    return cliConfig

def parseFile(config, clearText):
    file = open(config, "rt", encoding="UTF8")
    contents = file.read()
    Parser.runParser(contents, cliConfig["outputFile"])
    return print("not done yet")