#Aqui vão todas as funções de embelezamento de código;

def ltela():
  from os import system, name
  """
  O nome é um tanto quanto autoexplicativo, é basicamente uma função para limpar a tela,
  sendo assim não tem passagem de parâmetro ou retorno.
  #FUNCIONANDO CORRETAMENTE#
  """
  if name == 'nt':
    _ = system('cls')
    
  else:
    _ = system('clear')


def colorizar(texto, es='normal', corl='branco', corf=0):
  estilo = {'normal': 0, 'negrito': 1, 'sublinhado': 4, 'negativo': 7}
  corletra = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33, 'azul': 34, 'lilas': 35, 'ciano': 36, 'cinza': 37}
  corfundo = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43, 'azul': 44, 'lilas': 45, 'ciano': 46, 'cinza': 47}
  if corf != 0:
    print(f'\033[{estilo[es]};{corletra[corl]};{corfundo[corf]}m{texto}\033[m')
  else:
    print(f'\033[{estilo[es]};{corletra[corl]}m{texto}\033[m')