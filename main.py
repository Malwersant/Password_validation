password = 'kotas'
user_password = input('Proszę o podanie hasła: ')

if user_password == password:
    print('Gratulacje, PIN jest poprawny!')
else:
    count = 1
    while count < 3:
        user_password = input(f'Hasło nieprawidłowe. Zostało ci jeszcze {3 - count} prób. Proszę o ponowne podanie hasła: ')
        if user_password == password:
            print('Gratulacje, PIN jest poprawny!')
            break
        count += 1

    if count == 3:
        print('Podałeś 3 razy nierprawidłowe hasło. Karta została zablokowana.')
