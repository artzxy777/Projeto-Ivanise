import time
import random

# Inicialização do sistema
time.sleep(1)
print("====== Inicializando sistema ======")
time.sleep(1)
print("====== Sucesso! ======\n")
time.sleep(1)
print("====== Carregando Agendamentos ======")
time.sleep(1)
print("====== Sucesso! ======\n")
time.sleep(1)
print("====== Carregando informações do cliente ======")
time.sleep(1)
print("====== Sucesso! ======\n")
time.sleep(2)
print("=================== Bem vindo ao lava Jato Odebrecht ===================\n")


# Informações do cliente
while True:
    nome = input("Digite seu nome: ").strip()
    if nome and not any(caractere.isdigit() for caractere in nome):
        break
    print("Erro: digite um nome válido, sem números e sem deixar em branco.")


# Informações do carro
while True:
    carro = input(
        "\nEscolha as opções de carro: \n1 - Sedan\n2 - Hatch\n3 - SUV\n4 - Picape\n"
    ).strip()
    if carro in {"1", "2", "3", "4"}:
        break
    print("Erro: escolha apenas um número entre 1 e 4.")

# Cálculo do preço com base no tipo de carro
if carro == "1":
    fator_carro = 1.10
elif carro == "2":
    fator_carro = 1.00
elif carro == "3":
    fator_carro = 1.20
else:
    fator_carro = 1.30

preco_simples = 30.00 * fator_carro
preco_completa = 50.00 * fator_carro
preco_premium = 80.00 * fator_carro


# Informações do tipo de lavagem
while True:
    lavagem = input(
        f"\nEscolha o tipo de lavagem: \n"
        f"1 - Simples - R$ {preco_simples:.2f}\n"
        f"2 - Completa - R$ {preco_completa:.2f}\n"
        f"3 - Premium - R$ {preco_premium:.2f}\n"
    ).strip()
    if lavagem in {"1", "2", "3"}:
        break
    print("\nErro: escolha apenas um número entre 1 e 3.")

# Cálculo do preço com base no tipo de lavagem
if lavagem == "1":
    preco = preco_simples
elif lavagem == "2":
    preco = preco_completa
else:
    preco = preco_premium


# Informações do agendamento
dias_semana = {
    "1": "Segunda-feira",
    "2": "Terça-feira",
    "3": "Quarta-feira",
    "4": "Quinta-feira",
    "5": "Sexta-feira",
    "6": "Sábado",
    "7": "Domingo",
}

# Gerando disponibilidade aleatória para os dias da semana
dias_uteis = ["1", "2", "3", "4", "5"]
feriado = random.choice(dias_uteis)
disponibilidade = {
    dia: random.choice([True, False]) for dia in dias_semana
}
disponibilidade[feriado] = True

# Exibindo disponibilidade para agendamento
print("\nDisponibilidade para agendamento:")
for dia, nome_dia in dias_semana.items():
    if dia == feriado:
        status = "Disponível - Feriado"
    elif disponibilidade[dia]:
        status = "Disponível"
    else:
        status = "Indisponível"
    print(f"{dia} - {nome_dia}: {status}")

# Solicitando ao usuário que escolha um dia disponível para o agendamento
while True:
    agendamento = input(
        "\nEscolha um dia disponível para o agendamento: "
    ).strip()
    if agendamento in dias_semana and disponibilidade[agendamento]:
        break
    print("\nErro: esse dia está indisponível ou a opção é inválida.")

print(f"\nVocê escolheu agendar para {dias_semana[agendamento]}.")


# Informações do tipo de pagamento
while True:
    pagamento = input(
        "\nEscolha o tipo de pagamento: \n1 - Dinheiro\n2 - Cartão\n3 - Pix\n").strip()
    if pagamento in {"1", "2", "3"}:
        break
    print("\nErro: escolha apenas um número entre 1 e 3.")


# Descontos e acréscimos
if pagamento == "1":
    desconto = 0.10
elif pagamento == "2":
    desconto = -0.1
else:
    desconto = 0.10

# Cálculo do valor final com base no tipo de pagamento e agendamento
acrescimo_agendamento = 0
if agendamento in {"6", "7"}:
    acrescimo_agendamento += 0.10
if agendamento == feriado:
    acrescimo_agendamento += 0.15

valor_final = preco * (1 - desconto + acrescimo_agendamento)


nomes_carros = {
    "1": "Sedan",
    "2": "Hatch",
    "3": "SUV",
    "4": "Picape",
}
nomes_lavagens = {
    "1": "Simples",
    "2": "Completa",
    "3": "Premium",
}
nomes_pagamentos = {
    "1": "Dinheiro",
    "2": "Cartão",
    "3": "Pix",
}

# Loop para confirmação e possíveis alterações
while True:
    print("\n========== Resumo do agendamento ==========")
    print(f"Cliente: {nome}")
    print(f"Carro: {nomes_carros[carro]}")
    print(f"Lavagem: {nomes_lavagens[lavagem]}")
    print(f"Dia: {dias_semana[agendamento]}")
    print(f"Pagamento: {nomes_pagamentos[pagamento]}")
    print(f"Valor final: R$ {valor_final:.2f}")

    # Loop para confirmação das informações
    while True:
        confirmacao = input(
            "\nConfirma as informações? (S/N): "
        ).strip().lower()
        if confirmacao in {"s", "n"}:
            break
        print("\nErro: responda apenas com S para sim ou N para não.")

    if confirmacao == "s":
        print("\nAgendamento confirmado com sucesso!")
        break

    # Opções de alteração
    print("\nO que você deseja alterar?")
    print("1 - Nome")
    print("2 - Modelo do carro")
    print("3 - Tipo de lavagem")
    print("4 - Dia do agendamento")
    print("5 - Forma de pagamento")
    print("6 - Tava so olhando, vou sair e ir no concorrente mesmo.")

    # Caso o cliente coloque um numero inválido, o sistema vai pedir para ele colocar novamente
    while True:
        alteracao = input("\nEscolha uma opção: ").strip()
        if alteracao in {"1", "2", "3", "4", "5", "6"}:
            break
        print("\nErro: escolha uma opção entre 1 e 6.")

    # Resposta Concorrente
    if alteracao == "6":
        print("\nQue pena! Esperamos que volte em breve.")
        break

    # Loop Para o Nome
    if alteracao == "1":
        while True:
            nome = input("Digite seu nome: ").strip()
            if nome and not any(caractere.isdigit() for caractere in nome):
                break
            print("Erro: digite um nome válido, sem números e sem deixar em branco.")

    # Loop Para o Modelo do Carro
    elif alteracao == "2":
        while True:
            carro = input(
                "Escolha o modelo: \n1 - Sedan\n2 - Hatch\n3 - SUV\n4 - Picape\n"
            ).strip()
            if carro in {"1", "2", "3", "4"}:
                break
            print("Erro: escolha apenas um número entre 1 e 4.")

        # Cálculo do preço com base no tipo de carro 2
        if carro == "1":
            fator_carro = 1.10
        elif carro == "2":
            fator_carro = 1.00
        elif carro == "3":
            fator_carro = 1.20
        else:
            fator_carro = 1.30

        preco_simples = 30.00 * fator_carro
        preco_completa = 50.00 * fator_carro
        preco_premium = 80.00 * fator_carro
        if lavagem == "1":
            preco = preco_simples
        elif lavagem == "2":
            preco = preco_completa
        else:
            preco = preco_premium

    # Loop Para o Tipo de Lavagem
    elif alteracao == "3":
        while True:
            lavagem = input(
                f"1 - Simples - R$ {preco_simples:.2f}\n"
                f"2 - Completa - R$ {preco_completa:.2f}\n"
                f"3 - Premium - R$ {preco_premium:.2f}\n"
                "Escolha o tipo de lavagem: "
            ).strip()
            if lavagem in {"1", "2", "3"}:
                break
            print("Erro: escolha apenas um número entre 1 e 3.")
        if lavagem == "1":
            preco = preco_simples
        elif lavagem == "2":
            preco = preco_completa
        else:
            preco = preco_premium

    # Loop Para o Dia do Agendamento
    elif alteracao == "4":
        print("\nDisponibilidade para agendamento:")
        for dia, nome_dia in dias_semana.items():
            if dia == feriado:
                status = "Disponível - Feriado"
            elif disponibilidade[dia]:
                status = "Disponível"
            else:
                status = "Indisponível"
            print(f"{dia} - {nome_dia}: {status}")

        while True:
            novo_dia = input("\nEscolha um dia disponível: ").strip()
            if novo_dia in dias_semana and disponibilidade[novo_dia]:
                agendamento = novo_dia
                break
            print("Erro: esse dia está indisponível ou a opção é inválida.")
        print(f"Você escolheu agendar para {dias_semana[agendamento]}.")

    # Loop Para o Tipo de Pagamento
    else:
        while True:
            pagamento = input(
                "1 - Dinheiro\n2 - Cartão\n3 - Pix\nEscolha o pagamento: "
            ).strip()
            if pagamento in {"1", "2", "3"}:
                break
            print("Erro: escolha apenas um número entre 1 e 3.")

    if pagamento == "1":
        desconto = 0.10
    elif pagamento == "2":
        desconto = -0.1
    else:
        desconto = 0.10

    acrescimo_agendamento = 0
    if agendamento in {"6", "7"}:
        acrescimo_agendamento += 0.10
    if agendamento == feriado:
        acrescimo_agendamento += 0.15
    valor_final = preco * (1 - desconto + acrescimo_agendamento)
