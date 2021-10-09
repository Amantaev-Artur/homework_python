def f(d, m, y):
    '''
    В функцию поступают три целочисленные переменые: день, месяц, год
    Функция возвращает значение True или False - существует ли такая дата
    '''
    listbig = [1,3,5,7,8,10,12]
    listsmall = [4,6,9,11]
    d_now = 9
    m_now = 10
    y_now = 2021
    if (y > 0 and m > 0 and d > 0 and m < 13 and d < 32) and (y <= y_now):
        if (y < y_now) or (y == y_now and m < m_now) or (y == y_now and m == m_now and d <= d_now):
            if d < 31 and m in listsmall:
                return True
            elif d < 32 and m in listbig:
                return True
            elif m == 2:
                if (d == 29 and y%4 == 0) or d < 29:
                    return True
    return False

print(f(21, 10 ,2021))