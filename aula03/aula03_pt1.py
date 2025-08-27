import time
from datetime import datetime, timedelta

class Cliente:
    def __init__(self, nome, protocolo):
        self.nome = nome
        self.protocolo = protocolo
        self.hora_chegada = datetime.now()
        self.hora_atendimento = None
        self.hora_saida = None

class Caixa:
    def __init__(self):
        self.cliente_atual = None
        self.hora_fim_atendimento = None

    def iniciar_atendimento(self, cliente_da_fila):

        print(f"[{datetime.now().strftime('%H:%M:%S')}] INICIANDO: Atendimento para {cliente_da_fila.nome}.")
        
        self.cliente_atual = cliente_da_fila
        
        self.cliente_atual.hora_atendimento = datetime.now()
        
        self.hora_fim_atendimento = self.cliente_atual.hora_atendimento + timedelta(seconds=10)

    def finalizar_atendimento(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] FINALIZADO: Atendimento de {self.cliente_atual.nome}.")
        
        self.cliente_atual.hora_saida = datetime.now()
        
        self.cliente_atual = None
        self.hora_fim_atendimento = None

nomes = ["Miguel", "Helena", "Arthur", "Alice", "Gael", 
        "Laura", "Heitor", "Maria Alice", "Theo", "Valentina", 
        "Davi", "Heloísa", "Gabriel", "Maria Clara", "Bernardo", 
        "Cecília", "Samuel", "Maria Cecília", "João Miguel", "Maite", 
        "Enzo Gabriel", "Antonella", "Pedro Henrique", "Isis", "Ravi", 
        "Liz", "Noah", "Maria Julia", "Benício", "Sophia"]

fila_de_espera = []
caixa_01 = Caixa()
protocolo_atual = 1
proxima_chegada = datetime.now()

print(">>> Simulação de Fila Iniciada. Pressione CTRL+C para sair. <<<")

while True:
    hora_atual = datetime.now()

    if caixa_01.cliente_atual and hora_atual >= caixa_01.hora_fim_atendimento:
        caixa_01.finalizar_atendimento()

    if hora_atual >= proxima_chegada and nomes:
        nome_novo_cliente = nomes.pop(0)
        novo_cliente = Cliente(nome=nome_novo_cliente, protocolo=protocolo_atual)
            
        fila_de_espera.append(novo_cliente)
            
        print(f"[{hora_atual.strftime('%H:%M:%S')}] CHEGADA: {novo_cliente.nome} (Protocolo:{protocolo_atual}) entrou na fila.")
            
        protocolo_atual += 1
        proxima_chegada = hora_atual + timedelta(seconds=2)
        
    if caixa_01.cliente_atual is None and len(fila_de_espera) > 0:
        proximo_cliente = fila_de_espera.pop(0)
        caixa_01.iniciar_atendimento(proximo_cliente)

    print(f"ESTADO -> Fila: {len(fila_de_espera)} pessoa(s) | Caixa: {'Ocupado com ' + caixa_01.cliente_atual.nome if caixa_01.cliente_atual else 'Livre'}")
        
    time.sleep(1)