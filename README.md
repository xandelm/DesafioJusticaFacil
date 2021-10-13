# DesafioJusticaFacil
## Introdução
Este repositório foi desenvolvido como parte do processo seletivo de estágio para a empresa Justiça Fácil.

Os [diários oficiais](https://pt.wikipedia.org/wiki/Di%C3%A1rio_Oficial) são jornais criados, mantidos e administrados por governos para publicar as literaturas dos atos oficiais da administração pública executiva, legislativa e judiciária.

Todos os dias, o sistema desenvolvido pelo [Justiça Fácil](justicafacil.com.br) tem que verificar se os diários do Supremo Tribunal Federal foram baixados corretamente.
Para evitar que o mesmo diário seja processado mais de uma vez, foi desenvolvido por este candidato um programa escrito em python 3 que auxilia na conferência dos diários baixados pelo sistema.

O script desafio.py recebe uma data de disponibilização (data em que o diário foi colocado no sistema do tribunal) e retorna os hashes [MD5](https://pt.wikipedia.org/wiki/MD5) dos diários disponibilizados na data buscada.


## Uso
Para usar o programa, basta colocar o arquivo desafio.py no mesmo diretório(pasta) onde se encontram os diários oficiais baixados.
Então, execute o script informando a data já pela linha de comando, junto a execução do script. Este aceita dois formatos: 
- dd-mm-aaaa 
- dd/mm/aaaa. 

Se for digitada uma data fora dos formatos aceitos, o programa avisará e informará o usuário do formato correto a ser utilizado. O programa também avisa se não houver nenhum diário oficial baixado no diretório deste(excluindo diários que já foram renomeados para o seu respectivo hash MD5).

Se houverem diários baixados, mas nenhum com a data especifica buscada, o programa também avisará o usuário.

Se existir um diário oficial correspondente a data de busca informada, o programa irá imprimir uma lista de hash MD5 dos PDFs destes. Também irá renomear estes arquivos pdf para o seu respectivo hash MD5.

Segue um flowchart detalhando diferentes exemplos de entradas:

```mermaid
graph LR
A(Entrada:) -- python desafio.py 06/10/2021 --> H((Diretório com diários))--> B(Gera o hash e renomeia os arquivos se estiverem presentes)
A(Entrada:) -- python desafio.py 06/10/2021 --> F((Diretório sem diários)) --> G[Não há diários oficiais baixados neste diretório.]
A(Entrada:) -- python desafio.py --> C[Digite uma data ao rodar o script, no formato dd-mm-aaaa ou dd/mm/aaaa.]
A(Entrada:) --python desafio.py 28/01/1999 --> E
A(Entrada:) --python desafio.py entradaerrada --> I[Entrada inválida. Digite a data no formato:dd-mm-aaaa ou dd/mm/aaaa]

B --> D{Imprime o hash}
E[Não existem diários oficiais baixados correspondentes com a data buscada.]

