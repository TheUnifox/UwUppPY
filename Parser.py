
def runParser(contents: str, outputFileName: str):
    global outputFile; outputFile = open(outputFileName, "wt", encoding="UTF8"); outputFile.write(f"import random\n")
    skipLine = False
    for line in contents.splitlines():
        if line.find("UwU?") != -1:
            parseLine(line[0:line.find("UwU?")])
        elif (line.find("( ͡° ͜ʖ ͡°)") != -1) and not skipLine:
            parseLine(line[0:line.find("( ͡° ͜ʖ ͡°)")])
            skipLine = True
        elif (line.find("( ͡° ͜ʖ ͡°)") != -1) and skipLine:
            skipLine = False
            parseLine(line[(line.find("( ͡° ͜ʖ ͡°)")+11):])
        elif skipLine:
            continue
        else:
            parseLine(line)
    outputFile.close()

def parseLine(line: str):
    if line != "":
        line = line.replace("nuzzels(", "print(")

        line = line.replace("wetuwn", "    return")

        if line.strip().startswith("OwO *notices") or line.strip().startswith("UwU *notices") or line.strip().startswith("*notices") or line.strip().startswith("*owe notices") or line.strip().startswith("nyaa *"):
            line = line.rstrip("*")
            line = line + ":"

        line = line.replace("stawp", "")
    
        line = line.replace("nowt", "not")
        line = line.replace("newgatwive", "-")
        line = line.replace("iws", "=")
        line = line.replace("pwus", "+")
        line = line.replace("minwus", "-")
        line = line.replace("twimes", "*")
        line = line.replace("diwide", "/")
        line = line.replace("wemaindew", "%")
        line = line.replace("awway<", "[None] * ")
        line = line.replace(">", "")
        line = line.replace("OwO *notices", "while")
        line = line.replace("UwU *notices", "for")
        line = line.replace("*notices", "if")
        line = line.replace("*owe notices", "elif")
        line = line.replace("*owe*", "else:")
        line = line.replace("nyaa *", "def ")
        line = line.replace("gweatew twan", ">")
        line = line.replace("wess twan", "<")
        line = line.replace("eqwall twoo", "==")
        line = line.replace("uneqwall twoo", "!=")
        line = line.replace("wisten(", "input(")
        line = line.replace("stwing(", "str(")
        line = line.replace("wandInt(", "random.randint(")
        line = line.replace("spwitwines(", "splitlines(")
        line = line.replace("twu", "True")
        line = line.replace("faws", "False")
        line = line.replace("spwit(", "split(")
        line = line.replace("wength(", "len(")
        line = line.replace("wist(", "list(")
        line = line.replace("dwictwonwawy(", "dict(")
        line = line.replace("owe", "or")
        line = line.replace("worw()", "lower()")
        line = line.replace("stwip(", "strip(")
        line = line.replace("iwn", "in")
        line = line.replace("cwontwinwue", "continue")
        line = line.replace("appwewnd(", "append(")
        line = line.replace("bweak", "break")

        if line.find("wistenInt(") != -1:
            beforep = line[0:line.find("wistenInt(")]
            prompt = line[(line.find("wistenInt(")+10):line.rfind(")")]
            line = f"{beforep}int(input({prompt}))"

        if line.find("wite(") != -1:
            fileName = line[(line.find("wite(")+5):line.find(",")]
            toWrite = line[(line.find(",")+1):line.rfind(")")]
            line = f"{line[0: len(line) - len(line.lstrip(' '))]}toWriteTo = open({fileName}, 'wt', encoding='UTF8') \n{line[0: len(line) - len(line.lstrip(' '))]}toWriteTo.write({toWrite}) \n{line[0: len(line) - len(line.lstrip(' '))]}toWriteTo.close()"

        if line.find("wead(") != -1:
            fileName = line[(line.find("wead(")+5):line.rfind(")")]
            line = f"{line[0: len(line) - len(line.lstrip(' '))]}toReadFrom = open({fileName}, 'rt', encoding='UTF8') \n{line[0:(line.find('wead('))]}toReadFrom.read() \n{line[0: len(line) - len(line.lstrip(' '))]}toReadFrom.close()"
        
        outputFile.write(f"{line}\n")
        
        return print(line)