def Host():
    print(' ┌Endereço IP do outro usuário──♥')
    host = input(' └──> ')
    while host == '':
        host = input(' └──> ')
    return host # Retorna Host

def Porta():
    print(' ┌Porta──♥')
    porta = input(' └──> ')
    if porta == '':
        porta = 5621
    return int(porta)
