'''Recebe uma data de disponibilização de diarios oficiais
do Supremo Tribunal Federal e retorna os MD5 dos diários 
do dia recebido.'''


import sys #possibilita entradas pela linha de comando.
import re #possibilita o uso de funcoes relacionadas a Regex

DATE_LENGTH = 8
datePatternRegex = re.compile(r'''(
(\d{2})             # primeiros dois digitos(dia)
(\/|-|\.|\s)        # separador
(\d{2})             # dois digitos do meio(mes)
(\/|-|\.|\s)        # separador
(\d{2})             # ultimos dois digitos(ano)
)''',re.VERBOSE)


date = sys.argv[1:] #passa a entrada da linha de comando para date(string)
try:
    if len(date[0]) != DATE_LENGTH :
        raise Exception('Data inválida. Digite a data no formato:00-00-00 ou 00/00/00')
except IndexError:
    print('Digite uma data ao rodar o script.')
    #propoe ao usuario a digitar a data no formato correto
match = re.search(datePatternRegex,date[0]) 
if match:       #verifica se a data foi digitada no formato correto
    print('O usuario digitou a data no formato correto.')
else:
    raise Exception('Data inválida. Digite a data no formato:00-00-00 ou 00/00/00')
    #propoe ao usuario a digitar a data no formato correto
