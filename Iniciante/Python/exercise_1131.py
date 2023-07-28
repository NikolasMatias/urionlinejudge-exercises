def isInterWinner(golsInter, golsGremio):
    return golsInter > golsGremio

def isGremioWinner(golsInter, golsGremio):
    return golsInter < golsGremio

def isGameTied(golsInter, golsGremio):
    return golsInter == golsGremio

grenais = []

while True:
    golsInter, golsGremio = [int(x) for x in input().split()]
    grenais.append([golsInter, golsGremio])

    print('Novo grenal (1-sim 2-nao)')

    if int(input()) != 1:
        break

interVictories = 0
gremioVictories = 0
tiedGames = 0

for grenal in grenais:
    golsInter, golsGremio = grenal
    if isInterWinner(golsInter, golsGremio):
        interVictories += 1
    elif isGremioWinner(golsInter, golsGremio):
        gremioVictories += 1
    elif isGameTied(golsInter, golsGremio):
        tiedGames += 1

print(''.join([str(len(grenais)), ' grenais']))
print(''.join(['Inter:',str(interVictories)]))
print(''.join(['Gremio:',str(gremioVictories)]))
print(''.join(['Empates:',str(tiedGames)]))

if interVictories == gremioVictories:
    print('Nao houve vencedor')
elif interVictories > gremioVictories:
    print('Inter venceu mais')
elif interVictories < gremioVictories:
    print('Gremio venceu mais')