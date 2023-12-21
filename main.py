password = 'kotas'
user_password = input('Proszę o podanie hasła: ')
# count = 1

if user_password == password:
    print('Gratulacje, PIN jest poprawny!')
else:
    count = 2
    user_password = input(f'Hasło nieprawidłowe. Zostało ci jeszcze {count} prób. Proszę o ponowne podanie hasła: ')
    while count < 3:
        if user_password == password:
            print('Gratulacje, PIN jest poprawny!')
            break

        else:
            user_password = input(f'Hasło nieprawidłowe. Zostało ci jeszcze {count - 1} prób. Proszę o ponowne podanie hasła: ')
        count += 1
        print('Podałeś 3 razy nierprawidłowe hasło. Karta została zablokowana.')

#
# Jeszcze nie działa przejście z drugiiego na trzeci licznik
# Mimo podania prawidłowego hasła w trzeciej próbie i tak dostaję komunikat, że  razy nieprawidłowe hasło podane i karta zablokowana.