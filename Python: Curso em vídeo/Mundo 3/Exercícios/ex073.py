# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#  a) Os 5 primeiros times.
#  b) Os últimos 4 colocados.
#  c) Times em ordem alfabética.
#  d) Em que posição está o time da -Chapecoense- Goiás. (vou mudar pq Chapecoense n ta na tabela

tabela = ("Palmeiras", "Grêmio", "Atlético-MG",
          "Flamengo", "Botafogo", "Bragantino",
          "Fluminense", "Athletico-PR", "Internacional",
          "Fortaleza", "São Paulo", "Cuiabá",
          "Corinthians", "Cruzeiro", "Vasco",
          "Bahia", "Santos", "Goiás",
          "Coritiba", "América-MG")

print(20*'=')
print(f"Os primeiros times são {tabela[0:5]}")

print(20*'=')
print(f"Os últmos times são {tabela[-4:]}")

print(20*'=')
print(f"Os times ordenados em ordem alfabética ficam: {sorted(tabela)}")

print(20*'=')
print(f"O Goiás está na {tabela.index('Goiás') + 1}° posição ")
