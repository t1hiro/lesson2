
def get_occupation(age):
    if age <= 0 or age > 122:
        return 'Передано некорретное значение'
    elif age <= 3:
        return 'Вы слишком малы'
    elif age <= 6:
        return 'Вы учитесь в детском саду'
    elif age <= 18:
        return 'Вы ходите в школу'
    elif age <= 22:
        return 'Вы учитесь в ВУЗе'
    elif age <= 65:
        return 'Вы работаете'
    else:
        return 'Вы на пенсии'

def check_age():
    print('Введите свой возраст')
    user_age = input()
    try:
        user_age = float(user_age)
        print(get_occupation(user_age))
    except ValueError:
        print('Некорректное значение - возраст должен быть числовым значением')

check_age()

