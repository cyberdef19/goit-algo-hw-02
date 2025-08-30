from application_queue.start_app import start_app
from pallindrom.start_app_pallindrom import start_app_pallindrom

if __name__ == '__main__':
    option = int(input("Оберіть програму, що має виконуватися:"
                       " 1 - програма імітації черги заявок"
                       " 2 - програма визначення чи є рядок палліндромом"))
    if option == 1:
        print("Виконуємо програмку імітації заявок")
        start_app()
    elif option == 2:
        print("Виконуємо програму визначення чи є рядок палліндромом")
        start_app_pallindrom()
    else:
        print("Ми навіть не знаємо, що ви побажали виконати?!))))")
