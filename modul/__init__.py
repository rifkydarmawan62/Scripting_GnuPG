from subprocess import run
from platform import system

def bersihkan_layar(teks : str | None = None):
    if system() == "Windows":
        run("cls", shell = True)
    else:
        run("clear", shell = True)
    if teks:
        print(teks)