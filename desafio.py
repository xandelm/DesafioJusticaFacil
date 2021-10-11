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

TAM_DATA = 10

mensagemErro1 = 'Data inválida. Digite a data no formato:dd-mm-aaaa ou dd/mm/aaaa'
mensagemErro2 = 'Digite uma data ao rodar o script, no formato dd-mm-aaaa ou dd/mm/aaaa.'

dataPatternRegex = re.compile(r'''(
(\d{2})             # primeiros dois digitos(dia, grupo 1)
(\/|-|\.|\s)        # separador
(\d{2})             # dois digitos do meio(mes, grupo 3)
(\/|-|\.|\s)        # separador
(\d{4})             # ultimos dois digitos(ano, grupo 5)
)''',re.VERBOSE)


diarioFileNameRegex = re.compile(r'''(
                                 (^DJE_) # os arquivos do diario oficial começam com os digitos DJE_
                                 (\d{4}) # ano. group(3) 
                                 (\d{2}) # mes. group(4)
                                 (\d{2}) # dias. group(5)
                                 _(\d+\.pdf$) # os arquivos serao terminados em pdf
                                 )''',re.VERBOSE)
try:
    terminalInput = sys.argv[1:]
    data = terminalInput[0] #passa a entrada da linha de comando para data(string)
    if len(data) != TAM_DATA :
        raise Exception(mensagemErro1)
    match = re.search(dataPatternRegex,data)
    if not match:
        raise Exception(mensagemErro1)
    #propoe ao usuario a rodar o scrip novamente digitando a data no formato correto
except IndexError:
    print(mensagemErro2)
    sys.exit(0)
    #propoe ao usuario a digitar uma data ao utilizar o script
except NameError: 
    print(mensagemErro2)
    sys.exit(0)


#for DiarioBaixado in Path.cwd().glob('DJE_*'):
#    ListaDiarios.append(DiarioBaixado)
#DiariosBaixados = list(Path.cwd().glob('DJE_*'))
#for x in range(len(ListaDiarios)):
#    print(ListaDiarios[x])

dataSemSeparadores = data[0:2] + data[3:5] + data[6:]
#ListaDiarios = []
listaDatasDiarios = []

for fileName in os.listdir(Path.cwd()): #Percorre os arquivos no diretório atual
    matchObj = diarioFileNameRegex.search(fileName) #verifica se há algum diario oficial presente
    if matchObj == None:
        continue #se nao for um diario oficial, inicie uma nova interação do loop
    dataArquivoAtual = matchObj.group(5) + matchObj.group(4) + matchObj.group(3) #data arquivo atual = string de ano + string de mes + string de dia
    listaDatasDiarios.append(dataArquivoAtual)
    if(dataArquivoAtual == dataSemSeparadores):
        #TODO chama a funcao de gerar hash
        print('A data buscada está presente no diretório')
    #ListaDiarios.append(fileName)

if len(listaDatasDiarios) == 0:
    print('Não há diários baixados neste diretório.')

#for x in range(len(ListaDiarios)):
#    print(ListaDiarios[x])



#os.listdir(Path.cwd()) will return a list of filename strings for each file in the path argument.
#for filename in os.listdir(Path.cwd()):

#p = Path('C:/Users/Al/Desktop')
#list(p.glob('*.txt'))
