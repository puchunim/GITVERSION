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



