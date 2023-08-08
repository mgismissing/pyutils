import colorama
colorama.init()
def info(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	if color: print(end=colorama.Fore.CYAN)
	print(f"{code}{div}{desc}", end=end)
def warn(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	if color: print(end=colorama.Fore.YELLOW)
	print(f"{code}{div}{desc}", end=end)
def err(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	if color: print(end=colorama.Fore.RED)
	print(f"{code}{div}{desc}", end=end)
def fatal(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	if color: print(end=colorama.Fore.BLACK+colorama.Back.RED)
	print(f"{code}{div}{desc}", end=end)