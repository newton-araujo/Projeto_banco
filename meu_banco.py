import time
from datetime import datetime
#Mês, dia e hora.
today = datetime.now()
dt = today.strftime("%b %d, %Y %H:%M:%S")

print('Bem vindo ao Meu Banco'.center(30, "-"), '\n')

menu = True
depóstio = 0
saque = 0
extrato = ""
saldo = 0
verificando = 0
diario = 0
limite = 500

print(f'Carregando...'.center(30,'='),'\n')
time.sleep(2)

# Menu recendo True, enquanto for verdadeiro vai executar bloco de código abaixo:
while menu:

    # Inicio do sistema
    print('Opções'.center(30, "-"))
    print("""
    [1]Depósito    [4]Saldo
    [2]Saque       [?] 
    [3]Extrato     [?]
    [0]Sair        [?] 
""")
    menu = int(input('Opção: '))  # Usuário vai digitar opção desejada.
    if menu == 1: #Opção 1 - Depósito
        depóstio = float(input('Qual valor do depósito R$ '))
        if depóstio > 0: # condição para efetuar depóstio
            print(f'Deseja depósitar? R$ {depóstio:.2f}')
            print('[1]SIM ou [2]NÃO'.center(30, '-'))
            verificando = int(input('1 ou 2: '))
            if verificando == 1: # Usuário informando que confirma o depósito
                saldo += depóstio # saldo recebendo depósito
                extrato += f"Depósito ----------- R${depóstio:.2f} - {dt}\n"
                print(f'Depósito no valor R$ {depóstio:.2f}')
                print(f'Saldo: R$ {saldo}')
            elif verificando == 2: # Caso usuário digite opção 2 irá cancelar o depósito
                print('Depósito cancelado')
                print(f"saldo R$ {saldo} \n")
                
    if menu == 2: # Opção 2 - Saque
        print('SAQUE'.center(30, '-'))
        saque = float(input('Valor: R$ ')) #Valor solicitado para saque.
        if saldo > 0:
            if saque <= limite and diario < 3:
                if saque > 0: # Condição para saque.
                    print(f"Deseja sacar o valor R$ {saque:.2f} ") 
                    print('[1] SIM ou [2] NÃO'.center(30, '-'))
                    verificando = int(input('1 ou 2: '))
                    if verificando == 1: #Usuário informando que confirma o saque
                        saldo -= saque # saldo recebendo saque
                        extrato += f"Saque -------------- R${saque} - {dt} \n1"
                        diario += 1
                        print(f"Saque realizado!!! \n")
                        print(f'Saldo: R$ {saldo:.2f}')
            else:
                print('Limite diario excedido')
        else:
            print(f"Sem saldo --- Saldo: R${saldo:.2f}")
            
    if verificando == 2: #Caso o usúario digitar 2 irá cancelar saque.
                print('Saque cancelado!!!')
    if menu == 3:
         print('Extrato'.center(30, '-'))
         print('Não foram localizadas movimentações' if not extrato else extrato)
         print(f'\nSaldo: R$ {saldo:.2f}')
         print("".center(30, "-"))

    if menu == 4: #Opção 4 - Saldo
        print(f'Saldo: R${saldo:.2f}')

    if menu > 6:
         print("Opção inválida!!!")    
    if menu == 0:  # condição de parada do loop.
        break

print("Meu banco agredece a sua visita!")
