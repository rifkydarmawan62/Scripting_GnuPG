from subprocess import run, CalledProcessError
from colorama import Fore, Back
from tkinter.filedialog import askdirectory as pilih_direktori
from os.path import exists
from os import remove
from platform import system

if system().lower() == "windows":
    def bersihkan_layar(teks : str | None = None):
        run("cls", shell = True)
        if teks:
            print(teks)
    bersihkan_layar(f"{Fore.LIGHTBLUE_EX}Tekan Alt + Tab untuk membuka jendela baru{Fore.RESET}")
    DIREKTORI_FOLDER = pilih_direktori(title = "Pilih lokasi unduhan file GnuPG disimpan").replace("/", "\\")
    if DIREKTORI_FOLDER:
        URL = "https://files.gpg4win.org/gpg4win-4.3.0.exe"
        LOKASI_UNDUHAN = f"{DIREKTORI_FOLDER}\\gpg4win-4.3.0.exe"
        PERINTAH = f"bitsadmin /transfer \"Mengunduh_GnuPG\" /download /priority FOREGROUND \"{URL}\" \"{LOKASI_UNDUHAN}\""
        print(f"Menjalankan perintah Windows Command Prompt [{Fore.BLACK}{Back.LIGHTYELLOW_EX}{PERINTAH}{Fore.RESET}{Back.RESET}] ...")
        try:
            run(PERINTAH, shell = True, check = True)
        except CalledProcessError:
            print(f"{Fore.LIGHTRED_EX}Gagal mengunduh GnuPG!{Fore.RESET}")
            if exists(LOKASI_UNDUHAN):
                remove(LOKASI_UNDUHAN)
        except KeyboardInterrupt:
            print(f"{Fore.LIGHTRED_EX}Unduhan GnuPG dihentikan!{Fore.RESET}")
            if exists(LOKASI_UNDUHAN):
                remove(LOKASI_UNDUHAN)
        else:
            print(f"Menjalankan perintah instalasi GnuPG [{Fore.BLACK}{Back.LIGHTYELLOW_EX}\"{LOKASI_UNDUHAN}\"{Fore.RESET}{Back.RESET}] ...")
            try:
                run(f"\"{LOKASI_UNDUHAN}\"", shell = True, check = True)
            except CalledProcessError:
                print(f"{Fore.LIGHTRED_EX}Gagal menjalankan instalasi GnuPG!{Fore.RESET}")
    else:
        print(f"{Fore.LIGHTRED_EX}Unduhan instalasi GnuPG tidak disimpan!{Fore.RESET}")