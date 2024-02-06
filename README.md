# Tabela de pontos corridos Brasileirão
Nos campeonatos de futebol de pontos corridos, são contabilizados pontos referentes aos resultados que um time consegue durante a competição.

Neste contexto, considerando um campeonato com 20 times, onde cada time se enfrenta 2 vezes, 38 jogos são disputados por time.

A pontuação é definida por um sitema em que as vitórias valem 3 pontos, os empates 1 ponto e em caso de derrota nenhum ponto é adicionado.

Em casos que a pontuação de 2 times fique igual, o primeiro critério de desempate é o número de vitórias e o segundo critério é pelo saldo de gols (gols marcados - gols sofridos) de um time.

![image](https://github.com/VMila/TesteUnitario/assets/95143973/31b2c78a-3a6a-4487-a250-b33ca0ff2cb5)

# Testes feitos

Sabendo do que se trata a aplicação, a classe de TimeTabela é inicializada com as informações de um time até um momento X do campeonato.

4 funções são utilizadas para os testes

 1 - quantidadePontos( )

Faz os cálculos da pontuação de um time considerando suas vitórias, derrotas e empates. 

 2 - quantidadeJogos( )

Faz os cálculos da quantidade de jogos de um time somando suas vitórias, derrotas e empates.

 3 - comparaVencedor( )

Compara a pontuação de 2 times e os critérios de desempate para descobrir qual time esta na frente na tabela.

 4 - daPraAlcancar( )

Compara a pontuação de 2 times para saber se com a quantidade restante de jogos o time que está atrás na tabela ainda pode alcançar o outro. (Considerando que esses 2 times tenham a mesma quantidade de jogos)

# Execução do programa

python TesteUnitario.py -v
