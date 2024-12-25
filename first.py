#Замыкание для поиска среднего в аргументах.

def zamican():
    iashik = 0
    count = 0
    
    def sredn(curr):
        nonlocal iashik, count
        count += 1
        iashik += curr
        return (iashik / count)
    return sredn

nemagu = zamican()
sbogom = zamican()
nemagu(1)
sbogom(2)
nemagu(1)
sbogom(11)
nemagu(1)
sbogom(65)
nemagu(1)
print(sbogom(86))
print(nemagu(1))