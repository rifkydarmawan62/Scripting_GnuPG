from subprocess import CalledProcessError, run
from colorama import Fore, Back
from platform import system

def bersihkan_layar(teks : str | None = None):
    if system().lower() == "windows":
        run("cls", shell = True)
    else:
        run("clear", shell = True)
    if teks:
        print(teks)
bersihkan_layar(f"{Fore.YELLOW}Memeriksa perintah gpg ...{Fore.RESET}")
try:
    run("gpg --version", shell = True, check = True)
except CalledProcessError:
    print(f"{Fore.LIGHTRED_EX}Perintah gpg tidak ditemukan!{Fore.RESET}")
else:
    PERINTAH = "gpg --full-generate-key --verbose"
    print(f"{Fore.YELLOW}Menjalankan perintah {Fore.BLACK}{Back.LIGHTBLUE_EX}{PERINTAH}{Fore.RESET}{Back.RESET} {Fore.YELLOW}...{Fore.RESET}")
    try:
        run(PERINTAH, shell = True, check = True)
    except CalledProcessError:
        print(f"{Fore.LIGHTRED_EX}Gagal membuat sepasang kunci!{Fore.RESET}")
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}Sepasang kunci batal dibuat!{Fore.RESET}")
    else:
        print(f"{Fore.LIGHTGREEN_EX}Sepasang kunci berhasil dibuat!{Fore.RESET}")
    if system().lower() == "windows":
        NAMA_PROSES = "gpg-agent.exe", "keyboxd.exe"
        PERINTAH_HENTIKAN_PROSES = f"taskkill /F /IM \"{NAMA_PROSES[0]}\" & taskkill /F /IM \"{NAMA_PROSES[1]}\""
        print(f"{Fore.YELLOW}Menghentikan proses {Fore.BLACK}{Back.LIGHTYELLOW_EX}{NAMA_PROSES[0]}{Fore.YELLOW}{Back.RESET}, dan {Fore.BLACK}{Back.LIGHTYELLOW_EX}{NAMA_PROSES[1]}{Fore.YELLOW}{Back.RESET} menggunakan perintah Windows Command Prompt {Fore.BLACK}{Back.LIGHTBLUE_EX}{PERINTAH_HENTIKAN_PROSES}{Fore.YELLOW}{Back.RESET} ...{Fore.RESET}")
        try:
            run(PERINTAH_HENTIKAN_PROSES, shell = True, check = True)
        except CalledProcessError:
            print(f"{Fore.LIGHTRED_EX}Proses {Fore.BLACK}{Back.LIGHTYELLOW_EX}{NAMA_PROSES[0]}{Fore.LIGHTRED_EX}{Back.RESET} atau {Fore.BLACK}{Back.LIGHTYELLOW_EX}{NAMA_PROSES[1]}{Fore.LIGHTRED_EX}{Back.RESET} tidak ditemukan atau gagal dihentikan!{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}Proses {Fore.BLACK}{Back.LIGHTYELLOW_EX}{NAMA_PROSES[0]}{Fore.LIGHTGREEN_EX}{Back.RESET} atau {Fore.BLACK}{Back.LIGHTYELLOW_EX}{NAMA_PROSES[1]}{Fore.LIGHTGREEN_EX}{Back.RESET} berhasil dihentikan!{Fore.RESET}")