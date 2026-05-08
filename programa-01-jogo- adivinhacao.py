"""

# Programa 1: Jogo de Adivinhação

## Descrição do Sistema
Jogo interativo de adivinhação de números executado no terminal/Colab.
O jogador tenta descobrir um número secreto gerado aleatoriamente,
recebendo dicas a cada tentativa. O jogo possui 3 níveis de dificuldade
e exibe a pontuação ao final de cada rodada.

## Como utilizar
1. Execute a célula do código no Google Colab
2. Escolha o nível de dificuldade digitando 1, 2 ou 3
3. Digite seus palpites numéricos quando solicitado
4. Receba dicas se o número secreto é maior ou menor
5. Veja seu desempenho ao final e escolha se quer jogar novamente

## Como cada conteúdo exigido é usado no programa

### 3.1 — Estruturas de decisão simples e compostas
Usadas para verificar se o palpite é correto, maior ou menor que o
número secreto, exibindo mensagens diferentes em cada caso (if / if-else).

### 3.2 — Estruturas de decisão aninhadas e de múltipla escolha
Usadas para definir o intervalo e o número de tentativas conforme a
dificuldade escolhida (if / elif / else), e para classificar o
desempenho final do jogador (ótimo, bom ou fraco).

### 3.3 — Estruturas de repetição com variável de controle
O loop `for` controla e limita o número máximo de tentativas
permitidas por rodada, usando um contador incremental.

### 3.4 — Estruturas de repetição com teste no início
O loop `while` mantém o jogo rodando enquanto o jogador
quiser jogar novamente, testando a condição antes de cada rodada.
"""

import random

# ──────────────────────────────────────────────
# FUNÇÕES AUXILIARES
# ──────────────────────────────────────────────

def exibir_banner():
    print("=" * 50)
    print("        🎯 JOGO DE ADIVINHAÇÃO 🎯")
    print("=" * 50)

def escolher_dificuldade():
    """3.2 — Decisão de múltipla escolha com if/elif/else"""
    print("\nEscolha a dificuldade:")
    print("  1 - Fácil   (1 a 50,  10 tentativas)")
    print("  2 - Médio   (1 a 100,  7 tentativas)")
    print("  3 - Difícil (1 a 200,  5 tentativas)")

    # 3.4 — Repetição com teste no início: só sai quando a entrada for válida
    while True:
        escolha = input("\nDigite 1, 2 ou 3: ").strip()
        if escolha == "1":
            return 1, 50, 10, "Fácil"
        elif escolha == "2":
            return 1, 100, 7, "Médio"
        elif escolha == "3":
            return 1, 200, 5, "Difícil"
        else:
            print("❌ Opção inválida! Digite apenas 1, 2 ou 3.")

def classificar_desempenho(tentativas_usadas, max_tentativas):
    """3.2 — Decisão aninhada para avaliar o desempenho do jogador"""
    proporcao = tentativas_usadas / max_tentativas
    if proporcao <= 0.3:
        return "🏆 INCRÍVEL! Adivinhou super rápido!"
    elif proporcao <= 0.6:
        return "👍 BOM! Desempenho acima da média."
    else:
        return "😅 Conseguiu! Mas pode melhorar."

def jogar_rodada(minimo, maximo, max_tentativas):
    """Executa uma rodada completa do jogo"""
    numero_secreto = random.randint(minimo, maximo)
    acertou = False

    print(f"\n🔒 Número secreto gerado entre {minimo} e {maximo}.")
    print(f"   Você tem {max_tentativas} tentativas. Boa sorte!\n")

    # 3.3 — Repetição com variável de controle (for + contador de tentativas)
    for tentativa in range(1, max_tentativas + 1):
        print(f"--- Tentativa {tentativa} de {max_tentativas} ---")

        # Validação da entrada
        while True:
            try:
                palpite = int(input(f"Digite um número entre {minimo} e {maximo}: "))
                break
            except ValueError:
                print("⚠️  Digite apenas números inteiros!")

        # 3.1 — Decisão simples e composta (if/elif/else)
        if palpite == numero_secreto:
            print(f"\n✅ PARABÉNS! Você acertou em {tentativa} tentativa(s)!")
            print(classificar_desempenho(tentativa, max_tentativas))
            acertou = True
            break
        elif palpite < numero_secreto:
            # 3.1 — Decisão simples: dica adicional na última tentativa
            if tentativa == max_tentativas:
                print("❌ Errou! O número secreto era MAIOR. Sem mais tentativas!")
            else:
                print(f"📈 Muito baixo! Tente um número MAIOR. ({max_tentativas - tentativa} tentativa(s) restante(s))")
        else:
            if tentativa == max_tentativas:
                print("❌ Errou! O número secreto era MENOR. Sem mais tentativas!")
            else:
                print(f"📉 Muito alto! Tente um número MENOR. ({max_tentativas - tentativa} tentativa(s) restante(s))")

    # 3.1 — Decisão simples: revelar o número caso não tenha acertado
    if not acertou:
        print(f"\n💀 Que pena! O número secreto era: {numero_secreto}")

    return acertou

# ──────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ──────────────────────────────────────────────

def main():
    exibir_banner()

    vitorias = 0
    derrotas = 0

    # 3.4 — Repetição com teste no início: joga enquanto o usuário quiser
    jogar_novamente = True
    while jogar_novamente:
        minimo, maximo, max_tentativas, nivel = escolher_dificuldade()
        print(f"\n🎮 Nível: {nivel}")

        resultado = jogar_rodada(minimo, maximo, max_tentativas)

        # 3.1 — Decisão simples para atualizar placar
        if resultado:
            vitorias += 1
        else:
            derrotas += 1

        print(f"\n📊 Placar: {vitorias} vitória(s) | {derrotas} derrota(s)")

        # 3.4 — Teste no início: verifica se quer continuar
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()

        # 3.2 — Decisão composta
        if resposta == "s":
            jogar_novamente = True
            print("\n" + "=" * 50)
        else:
            jogar_novamente = False

    print("\n👋 Obrigado por jogar! Até a próxima.")
    print(f"🏅 Resultado final: {vitorias} vitória(s) e {derrotas} derrota(s).")

main()