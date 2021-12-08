# 1. Програма-банкомат.
#   Створити програму з наступним функціоналом:
#      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#   Особливості реалізації:
#      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#   Особливості функціонала:
#      - за кожен функціонал відповідає окрема функція;
#      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#      - потім - елементарне меню типа:
#        Введіть дію:
#           1. Продивитись баланс
#           2. Поповнити баланс
#           3. Вихід
#      - далі - фантазія і креатив :)

import json

def add_new_user(username, password):
    base = {"username": username, "password": password}

    with open("users.data", "r") as users_file_add:
        later_base = json.load(users_file_add)
        later_base.append(base)

    with open("users.data", "w+") as users_file_add:
        base_js = json.dumps(later_base)
        users_file_add.write(base_js)
#    with open("users.data", "a") as users_file_add:
#       users_file_add.write(base_js)
    with open("{}_balance.data".format(username), "w") as username_balance:
        username_balance.write("0")
    with open("{}_transactions.data".format(username), "a") as username_transactions:
        username_transactions.write("Date of create")


def check_balance(username):
    with open ("{}_balance.data".format(username), "r") as balance:
        result_to_print = json.load(balance)
        print(result_to_print)


def up_balance(username):
    sum_to_up = input("Введіть суму, на яку хочете поповнити: ")
    if sum_to_up.isdigit():
        sum_to_up = int(sum_to_up)
    else:
        print("Можна ввести лише число")

    with open("{}_balance.data".format(username), "r") as balance:
        remainder = int(json.load(balance))
        finish_sum = remainder + sum_to_up;

    with open("{}_balance.data".format(username), "w+") as balance:
        balance.write(str(finish_sum))

def down_balance(username):
    sum_to_down = input("Введіть суму, на яку хочете зняти: ")
    if sum_to_down.isdigit():
        sum_to_down = int(sum_to_down)
    else:
        print("Можна ввести лише число")

    with open("{}_balance.data".format(username), "r") as balance:
        remainder = int(json.load(balance))
        if remainder >= sum_to_down:
            finish_sum = remainder - sum_to_down;
        else:
            print("Недостатньо грошей")

    with open("{}_balance.data".format(username), "w+") as balance:
        balance.write(str(finish_sum))




def exit_from_menu():
    raise SystemExit


def start():
    username = input("Please, your login: ")
    password = int(input("Please, your password: "))
    with open("users.data", "r") as users_file:
        users_file_py = json.load(users_file)
        check = False
        for i in users_file_py:
            if i["username"] == username and i["password"] == password:
                print("Вхід успішний")
                check = True
        if check:
            print("1. Продивитись баланс\n2. Поповнити баланс\n3. Зняти кошти\n4. Вихід")
            operation = input("Виберіть операцію: ")
            if operation.isdigit():
                operation = int(operation)
            else:
                print("Введіть будь ласка число: ")
            if operation == 1:
                check_balance(username)
            if operation == 2:
                up_balance(username)
            if operation == 3:
                down_balance(username)
            if operation == 4:
                exit_from_menu()

        else:
            print("Пароль або логін введені неправильно")

#add_new_user("sasha", 1977)
start()








