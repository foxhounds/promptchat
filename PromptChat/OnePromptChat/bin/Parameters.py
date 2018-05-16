def Parameters():
    print(' ┌Seu endereço IP──♥')
    host = input(' └──> ')
    if host == '':
        host = '127.0.0.1'
    return host # Retorna Host

def Porta():
    print(' ┌Porta──♥')
    porta = input(' └──> ')
    if porta == '':
        porta = 5621
    return int(porta)
