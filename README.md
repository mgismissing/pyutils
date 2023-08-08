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
> This project is still in alpha.
## Utilities
In this section is listed every utility that you can find at the moment ordered in alphabetical order.
### Utility: status
#### Requirements
- colorama [`pip install colorama`]
#### Description
Make debugging easier with error logging. This logger has 4 highly-customizable statuses: info, warning, error and fatal.
#### Functions
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