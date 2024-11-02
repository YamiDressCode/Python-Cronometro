import os
import time
import threading

# Função para limpar a tela do console
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # 'cls' para Windows, 'clear' para Unix/Linux

class Cronometro:
    def __init__(self):
        # Inicialização das variáveis de tempo
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milissegundos = 0
        self.rodando = False  # Controla se o cronômetro está em execução
        self.pausado = False  # Controla se o cronômetro está pausado

    # Formata o tempo para exibição
    def formatar_tempo(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}.{self.milissegundos:03d}"

    # Incrementa o tempo (para cronômetro normal)
    def incrementar(self):
        self.milissegundos += 10
        if self.milissegundos >= 1000:
            self.milissegundos = 0
            self.segundos += 1
            if self.segundos >= 60:
                self.segundos = 0
                self.minutos += 1
                if self.minutos >= 60:
                    self.minutos = 0
                    self.horas += 1

    # Decrementa o tempo (para cronômetro regressivo)
    def decrementar(self):
        self.milissegundos -= 10
        if self.milissegundos < 0:
            self.milissegundos = 990
            self.segundos -= 1
            if self.segundos < 0:
                self.segundos = 59
                self.minutos -= 1
                if self.minutos < 0:
                    self.minutos = 59
                    self.horas -= 1

    # Executa o cronômetro
    def executar(self, regressivo=False):
        self.rodando = True
        while self.rodando:
            if not self.pausado:
                limpar_tela()
                print(self.formatar_tempo())
                if regressivo:
                    self.decrementar()
                    # Verifica se o tempo chegou a zero no modo regressivo
                    if self.horas == 0 and self.minutos == 0 and self.segundos == 0 and self.milissegundos == 0:
                        break
                else:
                    self.incrementar()
            time.sleep(0.01)  # Pausa de 10 milissegundos para controle de precisão

        if regressivo:
            print("Tempo esgotado!")

    # Alterna entre pausado e não pausado
    def pausar_continuar(self):
        self.pausado = not self.pausado

    # Para a execução do cronômetro
    def parar(self):
        self.rodando = False

# Função para o cronômetro normal
def cronometro_normal():
    crono = Cronometro()
    # Inicia o cronômetro em uma thread separada
    thread = threading.Thread(target=crono.executar)
    thread.start()
    
    # Loop para controle do usuário
    while True:
        comando = input("Digite 'p' para pausar/continuar ou 's' para sair: ").lower()
        if comando == 'p':
            crono.pausar_continuar()
        elif comando == 's':
            crono.parar()
            break

# Função para o cronômetro regressivo
def cronometro_regressivo():
    crono = Cronometro()
    # Solicita ao usuário o tempo inicial
    crono.horas = int(input("Digite o tempo em horas: "))
    crono.minutos = int(input("Digite o tempo em minutos: "))
    crono.segundos = int(input("Digite o tempo em segundos: "))
    crono.milissegundos = int(input("Digite o tempo em milissegundos: "))

    # Inicia o cronômetro regressivo em uma thread separada
    thread = threading.Thread(target=crono.executar, args=(True,))
    thread.start()
    
    # Loop para controle do usuário
    while True:
        comando = input("Digite 'p' para pausar/continuar ou 's' para sair: ").lower()
        if comando == 'p':
            crono.pausar_continuar()
        elif comando == 's':
            crono.parar()
            break

# Função principal
def main():
    print("===== CRONÔMETRO =====")
    print("1. Cronômetro Normal")
    print("2. Cronômetro Regressivo")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cronometro_normal()
    elif opcao == 2:
        cronometro_regressivo()
    else:
        print("Opção inválida!")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()