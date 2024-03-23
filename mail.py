COLOR_CODE = {
    "RESET": "\033[0m",  
    "BLUE": "\033[32m",     
    "BOLD": "\033[01m",
}

def get_mail(database_file, search_value):
    found = False

    with open(database_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')  
        if len(data) >= 8:
            email = data[8]
            if search_value in email:
                user_id = data[0]
                registration_date = data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                phone = data[7]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]  
                municipal_education = data[18]  
                institution_name = data[20]  

                print(f'''{COLOR_CODE["BLUE"]}
╔══════                                               ══════╗
║                                                           ║
                [+] ID пользователя: {user_id}
                [+] Дата регистрации: {registration_date}
                [+] Фамилия: {last_name}
                [+] Имя: {first_name}
                [+] Отчество: {middle_name}
                [+] Дата рождения: {birthday}
                [+] Пол: {gender}
                [+] Телефон: {phone}
                [+] Почта: {email}
                [+] Роль: {role}
                [+] Класс: {class_name}
                [+] Адрес: {address}
                [+] Страна: {country}
                [+] Гражданство: {citizenship}
                [+] Регион: {region}
                [+] Муниципальное образование: {municipal_education}
                [+] Наименование учреждения: {institution_name}  
║                                                           ║
╚══════                                               ══════╝
                     
                      ''')
                found = True

    if not found:
        print(f'{COLOR_CODE["GREEN"]}[ERROR] Ничего не найдено в базе данных по номеру телефона.')
