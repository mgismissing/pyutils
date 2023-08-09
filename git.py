import os
def clone(url) -> int:
    return os.system(f"git clone {url}")