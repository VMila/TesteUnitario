import unittest

class TimeTabela():
    def __init__(self, nome, vitorias, empates, derrotas, saldoGols):
        self.nome = nome
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas
        self.saldoGols = saldoGols
    
    def quantidadePontos(self):
        return self.vitorias*3 + self.empates
    
    def quantidadeJogos(self):
        return self.vitorias + self.empates + self.derrotas
    
    def comparaVencedor(self, outro):
        if(self.quantidadePontos() > outro.quantidadePontos()):
            return self.nome
        elif(self.quantidadePontos() < outro.quantidadePontos()):
            return outro.nome
        else:
            if(self.vitorias > outro.vitorias):
                return self.nome
            elif(self.vitorias < outro.vitorias):
                return outro.nome
            else:
                if(self.saldoGols > outro.saldoGols):
                    return self.nome
                else:
                    return outro.nome
    
    def daPraAlcancar(self, outro):
        diffPontos = self.quantidadePontos() - outro.quantidadePontos()
        partidasRestantes = 38 - self.quantidadeJogos()
        if(diffPontos > 0):
            if(diffPontos < partidasRestantes*3):
                return outro.nome + " pode alcancar"
            else:
                return outro.nome + " nao pode alcancar"
        else:
            if(-diffPontos < partidasRestantes*3):
                 return self.nome + " pode alcancar"
            else:
                return self.nome + " nao pode alcancar"
    
class TesteClass(unittest.TestCase):
    def testeQuemTaNaFrente(self):
        Time = TimeTabela("Sao Paulo", 20, 8, 10, 50)
        Outro = TimeTabela("Palmeiras", 19, 8, 11, 46)
        self.assertEqual("Sao Paulo", Time.comparaVencedor(Outro), "Time na frente errado!")
    def testeQuemTaNaFrentePorVitorias(self):
        Time = TimeTabela("Sao Paulo", 20, 6, 12, 50)
        Outro = TimeTabela("Palmeiras", 19, 9, 10, 50)
        self.assertEqual("Sao Paulo", Time.comparaVencedor(Outro), "Time na frente errado!")    
    def testeQuemTaNaFrentePorSaldoDeGols(self):
        Time = TimeTabela("Sao Paulo", 20, 6, 12, 50)
        Outro = TimeTabela("Palmeiras", 20, 6, 12, 46)
        self.assertEqual("Sao Paulo", Time.comparaVencedor(Outro), "Time na frente errado!")        
    def testeQuantidadeJogos(self):
        Time = TimeTabela("Sao Paulo", 20, 8, 10, 30)
        self.assertEqual(38, Time.quantidadeJogos(), "Quantidade de jogos errada!")
    def testeQuantidadePontos(self):
        Time = TimeTabela("Sao Paulo", 23, 8, 7, 30)
        self.assertEqual(77, Time.quantidadePontos(), "Quantidade de pontos errada!")    
    def testeNaoPodeAlcancar(self):
        Time = TimeTabela("Sao Paulo", 20, 5, 10, 50)
        Outro = TimeTabela("Palmeiras", 16, 6, 13, 20)
        self.assertEqual("Palmeiras nao pode alcancar", Time.daPraAlcancar(Outro), "Resultado incorreto!")    
    def testePodeAlcancar(self):
        Time = TimeTabela("Sao Paulo", 19, 5, 10, 50)
        Outro = TimeTabela("Palmeiras", 20, 6, 8, 20)
        self.assertEqual("Sao Paulo pode alcancar", Time.daPraAlcancar(Outro), "Resultado incorreto!")        
   

if __name__ == "__main__":
    unittest.main()