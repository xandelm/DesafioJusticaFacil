# DesafioJusticaFacil
## Introdução
Este repositório foi desenvolvido como parte de um desafio da Justiça Fácil.

Os [diários oficiais](https://pt.wikipedia.org/wiki/Di%C3%A1rio_Oficial) são jornais criados, mantidos e administrados por governos para publicar as literaturas dos atos oficiais da administração pública executiva, legislativa e judiciária.

Todos os dias, o sistema desenvolvido pelo [Justiça Fácil](justicafacil.com.br) tem que verificar se os diários do Supremo Tribunal Federal foram baixados corretamente.
Para evitar que o mesmo diário seja processado mais de uma vez, foi desenvolvido um programa escrito em python 3 que auxilia na conferência dos diários baixados pelo sistema.

O script desafio.py recebe uma data de disponibilização (data em que o diário foi colocado no sistema do tribunal), retorna os hashes [MD5](https://pt.wikipedia.org/wiki/MD5) dos diários disponibilizados na data buscada e renomeia os arquivos com seu respectivo hash.

## Uso
Para usar o programa, basta colocar o arquivo desafio.py no mesmo diretório(pasta) onde se encontram os diários oficiais baixados.
Então, execute o script informando a data já pela linha de comando, junto a execução do script. Este aceita dois formatos: 
- dd-mm-aaaa 
- dd/mm/aaaa. 

Se for digitada uma data fora dos formatos aceitos, o programa avisará e informará o usuário do formato correto a ser utilizado. O programa também avisa se não houver nenhum diário oficial baixado no diretório deste(excluindo diários que já foram renomeados para o seu respectivo hash MD5).

Se houverem diários baixados, mas nenhum com a data especifica buscada, o programa também avisará o usuário.

Se existir um diário oficial correspondente a data de busca informada, o programa irá imprimir uma lista de hash MD5 dos PDFs destes. Também irá renomear estes arquivos pdf para o seu respectivo hash MD5.

Segue um flowchart detalhando diferentes exemplos de entradas:

![Flowchart](https://i.imgur.com/tcf5zKy.jpg)


## Relatório de Desenvolvimento

Ao começar este desafio, foi realizada uma revisão de conceitos básicos da linguagem de programação python. Após cumprida a revisão, o desenvolvimento começou, com o início deste repositório e escrevendo um simples programa para receber entrada pela linha de comandos. Então, se tornou necessário aprender novos conceitos relacionados a regex para a continuação do desenvolvimento. Após muito estudo, foi possível completar o projeto, proporcionando ao candidato um aprendizado considerável sobre desenvolvimento de programas em python, o uso de novas bibliotecas e Regex.

### Recursos Utilizados
Este projeto foi desenvolvido utilizando um computador com sistema operacional Linux e no editor de texto NeoVim acessado por terminal UNIX. Foi utilizado a linguagem de programação Python versão 3.8.10.

Foram também acessadas diversas fontes de pesquisa, tanto para revisão de conhecimentos prévios como para a aquisição de novas habilidades e resolução de problemas, como:

- O livro  Automate the Boring Stuff with Python escrito por Al Sweigart.
- Diversos links do [StackOverflow](stackoverflow.com), [GeeksforGeeks](https://www.geeksforgeeks.org/) e [RealPython](realpython.com).

### Conclusão
A realização deste projeto se mostrou uma ótima oportunidade de relembrar conceitos assim como a aquisição de novos conhecimentos.
