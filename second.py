#Декоратор для проверки аргументов функции на тип и диапазон значений.

def prv(func):

    def wrapper(*args):
        print("Тип аргумента функции", type(*args))
        return func(*args)
    return wrapper

@prv
def func(arg):
    print(arg)

func([11,6,15,86])