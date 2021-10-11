'''
Recebe uma data de disponibilização de diarios oficiais
do Supremo Tribunal Federal e retorna os MD5 dos diários 
do dia recebido.
'''

import sys #possibilita entradas pela linha de comando.
import re #possibilita o uso de funcoes relacionadas a Regex
import os
from pathlib import Path
import shutil

DATE_LENGTH = 10
datePatternRegex = re.compile(r'''(
(\d{2})             # primeiros dois digitos(dia)
(\/|-|\.|\s)        # separador
(\d{2})             # dois digitos do meio(mes)
(\/|-|\.|\s)        # separador
(\d{4})             # ultimos dois digitos(ano)
)''',re.VERBOSE)


diarioFileNameRegex = re.compile(r'(^DJE_)(\d+)_(\d+\.pdf$)')

terminalInput = sys.argv[1:]
date = terminalInput[0] #passa a entrada da linha de comando para date(string)

print('date = '+date)
try:
    if len(date) != DATE_LENGTH :
        raise Exception('Data inválida. Digite a data no formato:dd-mm-aaaa ou dd/mm/aaaa')
except IndexError:
    print('Digite uma data ao rodar o script.')
    #propoe ao usuario a digitar a data no formato correto
match = re.search(datePatternRegex,date)
if not match:
    raise Exception('Data inválida. Digite a data no formato:dd-mm-aaaa ou dd/mm/aaaa')
    #propoe ao usuario a rodar o scrip novamente digitando a data no formato correto

ListaDiarios = []
#for DiarioBaixado in Path.cwd().glob('DJE_*'):
#    ListaDiarios.append(DiarioBaixado)
#DiariosBaixados = list(Path.cwd().glob('DJE_*'))
#for x in range(len(ListaDiarios)):
#    print(ListaDiarios[x])



for fileName in os.listdir(Path.cwd()): #Percorre os arquivos no diretório atual
    matchObj = diarioFileNameRegex.search(fileName) #verifica se há algum diario oficial presente
    if matchObj == None:
        continue #se nao for um diario oficial, inicie uma nova interação do loop

    ListaDiarios.append(fileName)

for x in range(len(ListaDiarios)):
    print(ListaDiarios[x])



#os.listdir(Path.cwd()) will return a list of filename strings for each file in the path argument.
#for filename in os.listdir(Path.cwd()):

#p = Path('C:/Users/Al/Desktop')
#list(p.glob('*.txt'))
