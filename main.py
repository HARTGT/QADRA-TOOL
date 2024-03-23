import os
from pystyle import Colorate, Colors

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(4):
        print()

    from banner import banner
    print(Colorate.Horizontal(Colors.red_to_yellow, banner.strip()))

    COLOR_CODE = {
        "BLUE": "\033[32m",
        "BOLD": "\033[01m",
        "RESET": "\033[0m",
    }

    prompt_text = f'{COLOR_CODE["BLUE"]}[+]{COLOR_CODE["BOLD"]} Выберите опцию'
    final_prompt = f"{prompt_text}{COLOR_CODE['BLUE']} > {COLOR_CODE['RESET']}"

    select = input(final_prompt)

    if select == '1':
        from search import get_number
        database_file = 'database.csv'
        search_value = input(f'{COLOR_CODE["BLUE"]}Введите номер телефона (формат: 79999999999): {COLOR_CODE["RESET"]}')
        get_number(database_file, search_value)
        input("Нажмите Enter, чтобы продолжить...")

    elif select == '2':
        from mail import get_mail
        database_file = 'database.csv'
        search_value = input(f'{COLOR_CODE["BLUE"]}Введите почту: {COLOR_CODE["RESET"]}')
        get_mail(database_file, search_value)
        input("Нажмите Enter, чтобы продолжить...")

    elif select == '3':
        from get_ip import get_ip
        get_ip()
        input("Нажмите Enter, чтобы продолжить...")

    elif select == '4':
        from ddos import dos
        dos()
        input("Нажмите Enter, чтобы продолжить...")

    elif select == '5':
        print(f'{COLOR_CODE["BLUE"]}Временно не доступно{COLOR_CODE["RESET"]}')
        input("Нажмите Enter, чтобы продолжить...")

    elif select == '6':
        exit()

    else:
        print(f'{COLOR_CODE["BLUE"]}Неверный выбор, попробуйте снова!{COLOR_CODE["RESET"]}')
