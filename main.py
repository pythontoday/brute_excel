import itertools
from string import digits, punctuation, ascii_letters
import win32com.client as client
from datetime import datetime
import time


def brute_excel_doc():
    print("***Hello friend!***")

    try:
        password_length = input("Введите длину пароля, от скольки - до скольки символов, например 3 - 7: ")
        password_length = [int(item) for item in password_length.split("-")]
    except:
        print("Проверьте введенные данные")

    print("Если пароль содержит только цифры, введите: 1\nЕсли пароль содержит только буквы, введите: 2\n"
          "Если пароль содержит цифры и буквы введите: 3\nЕсли пароль содержит цифры, буквы и спецсимволы введите: 4")

    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = "O.o что ты хочешь сынок?"
        # print(possible_symbols)
    except:
        print("O.o что ты хочешь сынок?")

    # brute excel doc
    start_timestamp = time.time()
    print(f"Started at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")

    count = 0
    for pass_length in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = "".join(password)
            # print(password)

            opened_doc = client.Dispatch("Excel.Application")
            count += 1

            try:
                opened_doc.Workbooks.Open(
                    r"C:\Users\User\PycharmProjects\brute_excel\fsociety.xlsx",
                    False,
                    True,
                    None,
                    password
                )

                time.sleep(0.1)
                print(f"Finished at - {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
                print(f"Password cracking time - {time.time() - start_timestamp}")

                return f"Attempt #{count} Password is: {password}"
            except:
                print(f"Attempt #{count} Incorrect password: {password}")
                pass


def main():
    print(brute_excel_doc())


if __name__ == '__main__':
    main()
