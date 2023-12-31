# PyUtils
A big library of utilities to make your python script lighter and easier to read.
## Installing PyUtils
### Method 1: using git
```bash
git clone https://github.com/mgismissing/pyutils
```
### Method 2: using the releases
Go in the [Releases](https://github.com/mgismissing/pyutils/releases) and download the latest version.  
> __Important__  
> This project is still being tested and it is in the alpha version. More information about PyUtils versions [here](https://github.com/mgismissing/pyutils/blob/main/VERSIONS.md)
## Utilities
In this section is listed every utility that you can find at the moment ordered in alphabetical order.
### Utility: git
#### Description
Clone repositories using git and print the output on the console.
#### Functions
```py
clone(url) -> int
```
clones a repository with the command `git clone` and prints the command's output on the console.
> __Warning__  
> This utility automatically runs code when imported in a project. [[See the code](https://github.com/mgismissing/pyutils/blob/main/AUTOCODE.md#utility-git)]  

> __Note__  
> This utility has been officially tested.
#### Information
Created 09/08/2023 by [mgismissing](https://github.com/mgismissing)  
Version 1.0
### Utility: status
#### Requirements
- colorama [`pip install colorama`]
#### Description
Make debugging easier by logging comments, variables, information, warnings, errors and fatal errors.
#### Functions
```py
comment(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")
```
displays a comment text, normally used for checking the flow of the code.  

`code`: the code number  
`desc`: the text shown after the code number  
`color`: whether or not should the text be grey  
`div`: the text between the code number and the description  
`end`: the text after the description 

```py
var(var = None, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")
```
displays the content of a variable, normally used for checking a variable's value.  

`var`: the variable  
`desc`: the text shown after the variable  
`color`: whether or not should the text be green  
`div`: the text between the variable and the description  
`end`: the text after the description 

```py
info(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")
```
displays an info text, normally used for logging information.  

`code`: the code number  
`desc`: the text shown after the code number  
`color`: whether or not should the text be cyan  
`div`: the text between the code number and the description  
`end`: the text after the description 

```py
warn(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")
```
displays a warning text, normally used for checks in the code or to log something that went wrong.  

`code`: the code number  
`desc`: the text shown after the code number  
`color`: whether or not should the text be yellow  
`div`: the text between the code number and the description  
`end`: the text after the description 

```py
err(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")
```
displays an error text, normally used for an exception in parts of the code with `try`/`except`.  

`code`: the code number  
`desc`: the text shown after the code number  
`color`: whether or not should the text be red  
`div`: the text between the code number and the description  
`end`: the text after the description  

```py
fatal(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")
```
displays a fatal error text, normally used for something that went terribly wrong in the code to the point that it cannot continue to work properly.  

`code`: the code number  
`desc`: the text shown after the code number  
`color`: whether or not should the text be red  
`div`: the text between the code number and the description  
`end`: the text after the description  
> __Warning__  
> This utility automatically runs code when imported in a project. [[See the code](https://github.com/mgismissing/pyutils/blob/main/AUTOCODE.md#utility-status)]  

> __Note__  
> This utility has been officially tested.
#### Information
Created 07/08/2023 by [mgismissing](https://github.com/mgismissing)  
Version 1.0