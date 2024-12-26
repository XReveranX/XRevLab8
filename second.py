#Декоратор для проверки аргументов функции на тип и диапазон значений.

def prv(func):

    def wrapper(*args):
        if (type(*args) != type(1)) and (type(*args) != type(1.1)):
            print("Ошибка, введите число.")
            return
        print("Тип аргумента функции", type(*args))
        return func(*args)
    return wrapper


def zamican():
    iashik = 0
    count = 0
    
    @prv
    def sredn(curr):
        nonlocal iashik, count
        count += 1
        iashik += curr
        return (iashik / count)
    return sredn


sbogom = zamican()
sbogom(2.0)
sbogom(11)
sbogom("RaaaaR")
sbogom(6.5)
print(sbogom(86))
