import sys
try:
	import colorama
	colorama.init(autoreset=True)
except ModuleNotFoundError:
	sys.exit("ModuleNotFoundError | status.py --> colorama: Missing library. Try installing it with pip [pip install colorama].")
def comment(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	"""Displays a comment text, normally used for checking the flow of the code."""
	print(f"{colorama.Fore.LIGHTBLACK_EX * color}{code}{div}{desc}", end=end)
def var(var = None, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	"""Displays the content of a variable, normally used for checking a variable's value."""
	print(f"{colorama.Fore.GREEN * color}{var}{div}{desc}", end=end)
def info(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	"""Displays an info text, normally used for logging information."""
	print(f"{colorama.Fore.CYAN * color}{code}{div}{desc}", end=end)
def warn(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	"""Displays a warning text, normally used for checks in the code or to log something that went wrong."""
	print(f"{colorama.Fore.YELLOW * color}{code}{div}{desc}", end=end)
def err(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	"""Displays an error text, normally used for an exception in parts of the code with try/except."""
	print(f"{colorama.Fore.RED * color}{code}{div}{desc}", end=end)
def fatal(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	"""Displays a fatal error text, normally used for something that went terribly wrong in the code to the point that it cannot continue to work properly."""
	print(f"{(colorama.Fore.WHITE + colorama.Back.RED) * color}{code}{div}{desc}", end=end)