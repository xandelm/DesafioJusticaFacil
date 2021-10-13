'''
Recebe uma data de disponibilização de diarios oficiais
do Supremo Tribunal Federal e retorna os hashes(MD5) dos diários
do dia recebido.
'''

import sys #possibilita entradas pela linha de comando.
import re #possibilita o uso de funcoes relacionadas a Regex
import os #possibilita o uso de funções do sistema operacional
from pathlib import Path #possibilita algumas funções para manipulação de arquivos e diretórios
import shutil #possibilita algumas operações em arquivos, em especial para renomear estes
import hashlib #possibilita algumas funções para gerar o hash MD5




def getDataFromTerminal(): #recebe uma data do usuário, pelo terminal/linha de comandos

    #formato de modelo regex da data
    dataPatternRegex = re.compile(r'''(
    (\d{2})             # primeiros dois digitos(dia, grupo 1)
    (\/|-|\.|\s)        # separador
    (\d{2})             # dois digitos do meio(mes, grupo 3)
    (\/|-|\.|\s)        # separador
    (\d{4})             # ultimos dois digitos(ano, grupo 5)
    )''',re.VERBOSE)

    TAM_DATA = 10 #tamanho da string da data que o usuário deve digitar
    mensagemErro1 = 'Data inválida. Digite a data no formato:dd-mm-aaaa ou dd/mm/aaaa'
    mensagemErro2 = 'Digite uma data ao rodar o script, no formato dd-mm-aaaa ou dd/mm/aaaa.'

    try:
        terminalInput = sys.argv[1:]
        data = terminalInput[0] #passa a entrada da linha de comando para data(string)
        if len(data) != TAM_DATA :
            raise Exception(mensagemErro1)
        match = re.search(dataPatternRegex,data)
        if match:
            return data
        else:
            raise Exception(mensagemErro1)
        #propoe ao usuario a rodar o scrip novamente digitando a data no formato correto
    except IndexError:
        print(mensagemErro2)
        sys.exit(0)
        #propoe ao usuario a digitar uma data ao utilizar o script
    except NameError: 
        print(mensagemErro2)
        sys.exit(0)


def generateMD5(fileName): #Recebe uma string e a retorna codificada em um hash MD5
    dataMD5 = hashlib.md5(fileName.encode())
    return dataMD5.hexdigest()


def getListas(data):
    '''retorna 3 listas
    primeira = lista de datas dos diarios no diretório
    segunda = lista de datas dos diarios no diretório correspondente com a busca
    terceira = lista dos hashes MD5 gerados
    '''
    #formato de modelo regex dos arquivos diarios baixados
    diarioFileNameRegex = re.compile(r'''(
                                  (^DJE_) # os arquivos do diario oficial começam com os digitos DJE_
                                  (\d{4}) # ano. group(3) 
                                  (\d{2}) # mes. group(4)
                                  (\d{2}) # dias. group(5)
                                  _(\d+\.pdf$) # os arquivos serao terminados em pdf
                                  )''',re.VERBOSE)



    dataSemSeparadores = data[0:2] + data[3:5] + data[6:] #remove os separadores e coloca no formato correto para comparação
    listaDatasDiarios = []
    listaDatasDiariosCorrespondentes = []
    listaHashesMD5 = []

    for fileName in os.listdir(Path.cwd()): #Percorre os arquivos no diretório atual
        matchObj = diarioFileNameRegex.search(fileName) #verifica se o arquivo é um diário oficial
        if matchObj == None:
            continue #se nao for um diario oficial, inicie uma nova interação do loop
        dataArquivoAtual = matchObj.group(5) + matchObj.group(4) + matchObj.group(3) #data arquivo atual = string de ano + string de mes + string de dia
        listaDatasDiarios.append(dataArquivoAtual)
        if(dataArquivoAtual == dataSemSeparadores): #se a data da busca e a data do arquivo forem correspondentes
            listaDatasDiariosCorrespondentes.append(dataArquivoAtual)
            hashGerado = generateMD5(fileName)
            listaHashesMD5.append(hashGerado)
            shutil.move(fileName,hashGerado) #renomeia o arquivo pdf para o seu hash MD5 correspondente
    return listaDatasDiarios, listaDatasDiariosCorrespondentes, listaHashesMD5


def printLista(lista):
    for valor in lista:
        print(valor)




data = getDataFromTerminal() #recebe uma data do usuário, pelo terminal/linha de comandos
listaDatasDiarios, listaDatasDiariosCorrespondentes, listaHashesMD5 = getListas(data)
if len(listaDatasDiariosCorrespondentes) == 0: #se nao existirem datas correspondentes com a busca
    if len(listaDatasDiarios) == 0: #se nao existirem diarios no diretório
        print('Não há diários oficiais baixados neste diretório.')
    else: # se existirem diários no diretório mas nenhum correspondente com a busca
        print('Não existem diários oficiais correspondentes com a data buscada.')
else: #se existe(m) arquivo(s) correspondente(s) com a busca
    printLista(listaHashesMD5)

