from subprocess import run, CalledProcessError
from colorama import Fore, Back
from tkinter.filedialog import askdirectory as pilih_direktori
from platform import system


def bersihkan_layar(teks : str | None = None):
    if system().lower() == "windows":
        run("cls", shell = True)
    else:
        run("clear", shell = True)
    if teks:
        print(teks)
if system().lower() == "windows":
    URL = "https://files.gpg4win.org/gpg4win-4.3.0.exe"
elif system().lower() == "linux":
    URL = "https://download.gnupg.com/files/gnupg/gnupg-desktop-2.4.3.0-x86_64.AppImage"
else:
    URL = "https://releases.gpgtools.com/GPG_Suite-2023.3.dmg"
bersihkan_layar(f"{Fore.LIGHTBLUE_EX}Tekan Alt + Tab untuk membuka jendela baru{Fore.RESET}")
DIREKTORI_FOLDER = pilih_direktori(title = "Pilih lokasi unduhan file GnuPG disimpan").replace("/", "\\")
if DIREKTORI_FOLDER:
    LOKASI_UNDUHAN = f"{DIREKTORI_FOLDER}\\{URL.split("/")[-1]}"
    if system().lower() == "windows":
        perintah = f"bitsadmin /transfer \"Mengunduh_Instalasi_GnuPG\" /download /priority FOREGROUND \"{URL}\" \"{LOKASI_UNDUHAN}\" && \"{LOKASI_UNDUHAN}\""
    else:
        perintah = f"cd \"{DIREKTORI_FOLDER}\"; curl --remote-name \"{URL}\""
        if system().lower() == "linux":
            perintah += f" && chmod +x \"{LOKASI_UNDUHAN}\"; \"{LOKASI_UNDUHAN}\""
    print(f"{Fore.YELLOW}Menjalankan perintah {"Windows Command Prompt" if system().lower() == "windows" else ""} {Fore.BLACK}{Back.LIGHTBLUE_EX}{perintah}{Fore.YELLOW}{Back.RESET} ...{Fore.RESET}")
    try:
        run(perintah, shell = True, check = True)
    except CalledProcessError:
        print(f"{Fore.LIGHTRED_EX}Gagal mengunduh atau menjalankan instalasi GnuPG!{Fore.RESET}")
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}Unduhan atau instalasi GnuPG dihentikan!{Fore.RESET}")
    else:
        print(f"{Fore.LIGHTGREEN_EX}Berhasil menjalankan instalasi GnuPG{Fore.RESET}")