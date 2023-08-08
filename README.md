# PyUtils
A big library of utilities to make your python script lighter and easier to read.
## Utilities
In this section is listed every utility that you can find at the moment ordered in alphabetical order.
### status
#### Requirements
- colorama | `pip install colorama`
#### Description
Make debugging easier with error logging. This logger has 4 highly-customizable statuses: info, warning, error and fatal.
#### Functions
- `info(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n")`: displays an info text.  
  `code`: the code number  
  `desc`: the text shown after the code number  
  `color`: whether or not should the text be cyan  
  `div`: the text between the code number and the description  
  `end`: the text after the description  
Other functions are present but are not shown here (001 not added yet)  
