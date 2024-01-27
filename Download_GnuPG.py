from subprocess import run, CalledProcessError
from colorama import Fore, Back
from tkinter.filedialog import askdirectory as pilih_direktori
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
        LOKASI_UNDUHAN = f"{DIREKTORI_FOLDER}\\{URL.split("/")[-1]}"
        PERINTAH = f"bitsadmin /transfer \"Mengunduh_GnuPG\" /download /priority FOREGROUND \"{URL}\" \"{LOKASI_UNDUHAN}\" && \"{LOKASI_UNDUHAN}\""
        print(f"{Fore.YELLOW}Menjalankan perintah Windows Command Prompt {Fore.BLACK}{Back.LIGHTBLUE_EX}{PERINTAH}{Fore.YELLOW}{Back.RESET} ...{Fore.RESET}")
        try:
            run(PERINTAH, shell = True, check = True)
        except CalledProcessError:
            print(f"{Fore.LIGHTRED_EX}Gagal mengunduh atau menjalankan instalasi GnuPG!{Fore.RESET}")
        except KeyboardInterrupt:
            print(f"{Fore.LIGHTRED_EX}Unduhan atau instalasi GnuPG dihentikan!{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}Berhasil menjalankan instalasi GnuPG{Fore.RESET}")