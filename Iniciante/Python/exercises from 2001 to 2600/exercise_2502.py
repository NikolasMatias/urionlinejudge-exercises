while True:
    try:
        qtdeCifras, qtdeFrases = [int(x) for x in input().split()]
        cifra1 = list(input()[:qtdeCifras])
        cifra2 = list(input()[:qtdeCifras])
        frases = [input() for x in range(qtdeFrases)]
        frasesDescriptografadas = []
        for frase in frases:
            frasesDescriptografadas.append([])
            indicesChanged = []
            characteres = list(frase)
            for indice_character in range(len(characteres)):
                character = characteres[indice_character]
                for indice in range(qtdeCifras):
                    if character == cifra1[indice] or character == cifra1[indice].lower():
                        frasesDescriptografadas[-1].append(character.replace(cifra1[indice].lower(), cifra2[indice].lower()).replace(cifra1[indice], cifra2[indice]))
                        indicesChanged.append(indice_character)
                    elif character == cifra2[indice] or character == cifra2[indice].lower():
                        frasesDescriptografadas[-1].append(character.replace(cifra2[indice].lower(),cifra1[indice].lower()).replace(cifra2[indice], cifra1[indice]))
                        indicesChanged.append(indice_character)
                    if indice_character in indicesChanged:
                        break
                if indice_character not in indicesChanged:
                    frasesDescriptografadas[-1].append(character)
                    indicesChanged.append(indice_character)
            print(''.join(frasesDescriptografadas[-1]))
        print()
    except EOFError:
        break