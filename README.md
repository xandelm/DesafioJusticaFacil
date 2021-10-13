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
-dd-mm-aaaa 
-dd/mm/aaaa. 
Se for digitada uma data fora dos formatos aceitos, o programa avisará e informará o usuário do formato correto a ser utilizado. O programa também avisa se não houver nenhum diário oficial baixado no diretório deste(excluindo diários que já foram renomeados para o seu respectivo hash MD5).

Se houverem diários baixados, mas nenhum com a data especifica buscada, o programa também avisará o usuário.

Se existir um diário oficial correspondente a data de busca informada, o programa irá imprimir uma lista de hash MD5 dos PDFs destes. Também irá renomear estes arquivos pdf para o seu respectivo hash MD5.
