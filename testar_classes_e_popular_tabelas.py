from cobrinha.config import *
from cobrinha.modelo import *

# cria um jogador
jogador1 = Jogador(nome="Jack Good", macas_coletadas= Jogador.macas_coletadas)
db.session.add(jogador1)
db.session.commit()

print(jogador1)
print("Dados inseridos")
