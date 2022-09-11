# Building / Installing #
### Reccomended: ### 
Download the [UwUpp.zip](https://github.com/TheUnifox/UwUppPY/releases/download/v0.1.1/UwUpp.zip) from [the most recent release](https://github.com/TheUnifox/UwUppPY/releases). Extract all contents to a folder of your choice. Then finally use the included install.ps1 to install UwU++. 
### Alternate: ### 
Download [the source zip](https://github.com/TheUnifox/UwUppPY/archive/refs/heads/main.zip) or clone this repo using [git](https://github.com/TheUnifox/UwUppPY/edit/main/ReadMe.md#with-git) or [github desktop](https://github.com/TheUnifox/UwUppPY/edit/main/ReadMe.md#or-github-desktop). Extract all contents to a folder of your choice. Then finally use [buildAndInstall.ps1](/buildAndInstall.ps1) to build and install UwU++ from source.\
\
You can now code in UwU++, and build it using ```UwUpp (your .uwu file name)```

# Cloning this repo #
### with git ###
use `git clone https://github.com/TheUnifox/UwUppPY.git` to clone this repo to a new UwUppPY folder in the current directory.\
use `git clone (release tag) https://github.com/TheUnifox/UwUppPY.git` to clone a specific release of this repo to a new UwUppPY folder in the current directory.\
use `git clone https://github.com/TheUnifox/UwUppPY.git (custom dir)` to clone this repo to a custom directory.
### or github desktop ###
click the green `Code` dropdown, then click `Open with Github Desktop`

# The Language Syntax #
## Basics ##
### While loop ###
```
OwO *notices (expression)*
  (loop body)
stawp (optional)
```
### For loop ###
```
UwU *notices (expression)*
  (loop body)
stawp (optional)
```
### If, Elif, and Else ###
``` 
*notices (expression)*
  (body)
 stawp (optional)
 
*owe notices (expression)*
  (body)
stawp (optional)

*owe*
  (body)
stawp (optional)
```
### Variable definition/assignment ###
`(variable name) iws (value)`
### Creating blank array/list and map/dictionary ###
#### array/list: #### 
`(variable name) iws awway<(size)>` <sup> <- this may be removed in the future </sup>\
or `(variable name) iws wist(*optional init list*)`
#### map/dict ####
`(variable name) iws dwictwonwawy(*optional init dict*)`
### Expressions ###
loop breaking `bweak`\
loop continuing `cwontwinwue`
#### if and while loop ####
`twu` and `faws`
```
nowt (expression)
(expression) owe (expression)
(variable) iwn (variable)
(variable) gweatew twan (variable)
(variable) wess twan (variable)
(variable) eqwall twoo (variable)
(variable) uneqwall twoo (variable)
```
#### for ####
```
(variable name) iwn (variable)
```
### Math ###
```
newgatwive
pwus (also for strings)
minwus
twimes
diwide
wemaindew
```
### String, List, and Dict functions ###
get lenght: `len(variable)`\
cast to string: `stwing(variable)`\
lowercase: `(stringVariable).wowew()`\
strip: `(stringVariable).stwip()`\
split: `(stringVariable).spwit()`\
split lines: `(stringVariable).spwitwines()`\
append: `(listOrDictVariable).appwewnd((variable))`
## More Advanced ##
### IO ###
output `nuzzels((output))` ex: `nuzzels("Hello World")`\
input `wisten((prompt))` ex: `wisten("Name?")`\
Int input `wistenInt((prompt))` ex: `wistenInt("Age?")`\
File write `wite((fileName), (toWrite))` ex: `wite("hello.txt", "Hello file!")`\
File read `variableName iws wead((fileName))` ex: `readFile iws wead("hello.txt")`
### function definition ###
```
nyaa *(funcName)((variables, comma seperated))*
  (body)
wetuwn (optional variable) (optional)
```
Ex:
```
nyaa *foo(varA, varB)*
  varC iws varA pwus varB
wetuwn varC
```
### Random functions ###
random integer: `wandInt()`

# Contributers and closing remarks #
Unifox(He/Him)#5654 on discord for this compiler and a BUNCH of functionality\
[Deltaphish](https://github.com/Deltaphish) here on github for [the original UwUpp](https://github.com/Deltaphish/UwUpp) done in Haskell
Hope you have fun trying to use this to code! :D
