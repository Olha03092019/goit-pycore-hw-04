from colorama import Fore, Back, Style
from pathlib import Path
import sys


def print_dir_structure(path):
    if not path.exists():
        print(f"{Fore.RED}[Шлях не існує: {path}]")
        return
    if path.is_file():
        print(f"{Fore.GREEN}{path.name}")
        return
    try:
            for item in path.iterdir():
                if item.is_dir():
                # Вивести директорію синім кольором
                 print(f"{Fore.BLUE}{item.name}")
                 # Рекурсія для виводу піддиректорій
                 print_dir_structure(item)
                  # Вивести файл зеленим кольором
                else: print(f"{Fore.GREEN}{item.name}")
    except PermissionError:
              print(f"{Fore.RED}[Доступ заборонено: {path}]")

def main():
    directory_path = Path(sys.argv[1])
    print(directory_path)
    print_dir_structure(Path(directory_path))

if __name__ == "__main__":
    main()
