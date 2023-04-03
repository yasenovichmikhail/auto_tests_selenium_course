

def line_cost(stroka):
    length = int(len(stroka))
    return print((length * 60)//100, 'р.', ((length*60)%100), 'коп.')

s = 'Я собираюсь сделать ему предложение, от которого он не сможет отказаться.'

line_cost(s)