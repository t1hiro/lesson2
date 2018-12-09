def get_occupation(user_age):
    try:
        user_age = float(user_age)
        if user_age <= 0 or user_age > 122:
            return 'Передано некорретное значение'
        elif user_age <= 3:
            return 'Вы слишком малы'
        elif user_age <= 6:
            return 'Вы учитесь в детском саду'
        elif user_age <= 18:
            return 'Вы ходите в школу'
        elif user_age <= 22:
            return 'Вы учитесь в ВУЗе'
        elif user_age <= 65:
            return 'Вы работаете'
        else:
            return 'Вы на пенсии'
    except ValueError:
        print('Некорректное значение - возраст должен быть числовым значением')


def check_age():
    print('Введите свой возраст')
    user_age = input()
    result = get_occupation(user_age)
    if result:
        print(result)


if __name__ == '__main__':
    check_age()
