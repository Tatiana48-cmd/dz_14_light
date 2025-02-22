import os
import pickle

def refill(balance):
    sum_popolnenie = int(input('Введите сумму пополнения: '))
    return balance + sum_popolnenie


def buying(balance, history):
    sum_buying = int(input('Введите сумму покупки: '))
    if sum_buying <= balance:
        name_buying = input('Введите название покупки: ')
        balance -= sum_buying

        history.append((name_buying, sum_buying))
        print(f'Покупка {name_buying} на сумму {sum_buying} рублей совершена.')
    else:
        print('Недостаточно средств!')
    return balance


def show_history(history):
    if history:
        print('История покупок:')
        for item, cost in history:
            print(f'{item}: {cost} рублей')
    else:
        print('История покупок пуста.')


def main():
    print('\n---------------------')

    # Проверяем, существует ли файл с балансом
    if os.path.exists('balance.data'):
        with open('balance.data', 'rb') as f:
            balance = pickle.load(f)
    else:
        balance = 0  # Устанавливаем баланс в ноль при первом запуске
        with open('balance.data', 'wb') as f:
            pickle.dump(balance, f)

    print(f'Исходный баланс {balance} рублей') # для обнуления баланса нужно удалить файл balance.data

    # Проверяем, существует ли файл с покупками
    if os.path.exists('history.data'):
        with open('history.data', 'rb') as f:
            history = pickle.load(f)
    else:
        history = []  # Устанавливаем историю покупок в ноль при первом запуске
        with open('history.data', 'wb') as f:
            pickle.dump(history, f)

    print(f'История покупок {history}')  # для обнуления истории покупок нужно удалить файл history.data

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            balance = refill(balance)
            print(f'На вашем счёте {balance} рублей')
            # Сохранение суммы счёта в файл
            with open('balance.data', 'wb') as f:
                pickle.dump(balance, f)
        elif choice == '2':
            balance = buying(balance, history)
            with open('balance.data', 'wb') as f:
                pickle.dump(balance, f)
            with open('history.data', 'wb') as f:
                pickle.dump(history, f)
        elif choice == '3':
            show_history(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


# Вызов main() только при прямом запуске модуля
if __name__ == '__main__':
    main()
