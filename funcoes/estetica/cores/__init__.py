from colorama import init
from os import name

if name == 'nt':
    init()
#CORES:
est = {'normal': 0, 'negrito': 1, 'sublinhado': 4, 'negativo': 7}
corl = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33, 'azul': 34, 'lilas': 35, 'ciano': 36, 'cinza': 37}
corf = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43, 'azul': 44, 'lilas': 45, 'ciano': 46, 'cinza': 47}

def branco(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["branco"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["branco"]}m{t}\033[m'
    else:
        return f'{t}'

def vermelho(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["vermelho"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["vermelho"]}m{t}\033[m'
    else:
        return f'{t}'

def verde(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["verde"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["verde"]}m{t}\033[m'
    else:
        return f'{t}'

def amarelo(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["amarelo"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["amarelo"]}m{t}\033[m'
    else:
        return f'{t}'

def azul(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["azul"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["azul"]}m{t}\033[m'
    else:
        return f'{t}'

def lilas(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["lilas"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["lilas"]}m{t}\033[m'
    else:
        return f'{t}'

def ciano(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["ciano"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["ciano"]}m{t}\033[m'
    else:
        return f'{t}'

def cinza(t, e='normal', cf='', disp=True):
    if disp == True:
        if cf != '':
            return f'\033[{est[e]};{corl["cinza"]};{corf[cf]}m{t}\033[m'
        else:
            return f'\033[{est[e]};{corl["cinza"]}m{t}\033[m'
    else:
        return f'{t}'


