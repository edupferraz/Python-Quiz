campeoes = {
    "Malphite", "Jax", "Kayle", "KSante", "KhaZik", "Graves", "LeeSin", "Kayn", "Hecarim", "Ahri",
    "Yasuo", "Zed", "Katarina", "AurelionSol", "Jhin", "Jinx", "Ezreal", "Caitlyn", "Kaisa",
    "Milio", "Thresh", "Lulu", "Nautilus", "Yuumi"
}

perguntas = [
    {
        "pergunta": "Qual lane você prefere?",
        "opcoes": [
            "a) Top",
            "b) Jungle",
            "c) Mid",
            "d) Adcarry",
            "e) Suporte"
        ],
        "pontuacao": {
            "a": {"Malphite", "Jax", "Kayle", "KSante"},
            "b": {"KhaZix", "Graves", "LeeSin", "Kayn", "Hecarim"},
            "c": {"Ahri", "Yasuo", "Zed", "Katarina", "Aurelion Sol"},
            "d": {"Jhin", "Jinx", "Ezreal", "Caitlyn", "Kaisa"},
            "e": {"Milio", "Thresh", "Lulu", "Nautilus", "Yuumi"}
        }
    },

    {
        "pergunta": "Prefere dano mágico ou dano físico?",
        "opcoes": [
            "a) Dano Mágico",
            "b) Dano Físico",
            "c) Gosto de mesclar os dois"
        ],
        "pontuacao": {
            "a": {"Ahri", "Aurelion Sol", "Ezreal", "Yuumi", "Milio", "Lulu", "Malphite", "Thresh", "Nautilus"},
            "b": {"Kayle", "KhaZix", "Graves", "Yasuo", "Zed", "Jhin", "Jinx", "Caitlyn", "Jax", "Ornn", "KSante", "Lee Sin", "Kayn", "Hecarim"},
            "c": {"Kaisa", "Katarina"},
        }
    },

    {
        "pergunta": "A primeira escolha de campeão seria?",
        "opcoes": [
            "a) Um campeão homem",
            "b) Uma campeã mulher",
            "c) Um campeão não humano"
        ],
        "pontuacao": {
            "a": {"Jax", "K'sante", "Graves", "Lee Sin", "Kayn", "Yasuo", "Zed", "Jhin", "Ezreal", "Milio", "Thresh"},
            "b": {"Kayle", "Ahri", "Katarina", "Jinx", "Caitlyn", "Kaisa"},
            "c": {"Malphite", "Ornn", "Kha'Zix", "Hecarim", "Aurelion Sol", "Lulu", "Yuumi", "Nautilus", }
        },
    },

]

respostas_jogador = []

for pergunta in perguntas:
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)
    resposta = input("Digite a letra correspondente à sua resposta: ")
    respostas_jogador.append(resposta)

# Calcular a pontuação com base nas respostas
pontuacao = {}

for i, resposta in enumerate(respostas_jogador):
    opcao = perguntas[i]["pontuacao"].get(resposta)
    if opcao:
        for campeao in opcao:
            if campeao in pontuacao:
                pontuacao[campeao] += 1
            else:
                pontuacao[campeao] = 1

# Exibir a pontuação final
print("Pontuação Final:")
for campeao, pontos in pontuacao.items():
    print(campeao + ": " + str(pontos))
