def function():
    dic_q = dict()
    name = ''
    nomer = ''
    while name != 'q' and nomer != 'q':
        name = input()
        if (name == 'q'):
            break
        nomer = input()
        if nomer == 'q':
            break
        if nomer[0]=='+' and nomer[1].isdigit and nomer[2]=="-" and nomer[3:6].isdigit and nomer[6]=='-' and nomer[7:10].isdigit and nomer[10]=='-' and nomer[11:13].isdigit and nomer[13]=='-' and nomer[14:] and len(nomer)==16:
            dic_q[name] = nomer
        else:
            print('Error')
    print(dic_q)



function()
