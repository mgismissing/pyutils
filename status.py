import colorama
colorama.init(autoreset=True)
def info(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	print(f"{colorama.Fore.CYAN * color}{code}{div}{desc}", end=end)
def warn(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	print(f"{colorama.Fore.YELLOW * color}{code}{div}{desc}", end=end)
def err(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	print(f"{colorama.Fore.RED * color}{code}{div}{desc}", end=end)
def fatal(code: int = 0, desc: str = "No description", color: bool = True, div: str = " ", end: str = "\n"):
	print(f"{(colorama.Fore.WHITE + colorama.Back.RED) * color}{code}{div}{desc}", end=end)