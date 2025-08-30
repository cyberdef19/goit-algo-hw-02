from pallindrom.pallindrom_processor import pallindrom_processor


def start_app_pallindrom():
    pallindrom_possible = input("Запишіть рядок, що претендує на роль палліндрома")
    if pallindrom_processor(pallindrom_possible):
        print("Вказаний рядок є палліндромом!")
    else:
        print("Вказаний рядок не є палліндромом!")
