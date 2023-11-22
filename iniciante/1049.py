aguia = ['vertebrado', 'ave', 'carnivoro', 'aguia']
pomba = ['vertebrado', 'ave', 'onivoro', 'pomba']

homem = ['vertebrado', 'mamifero', 'onivoro', 'homem']
vaca = ['vertebrado', 'mamifero', 'herbivoro', 'vaca']

pulga = ['invertebrado', 'inseto', 'hematofago', 'pulga']
lagarta = ['invertebrado', 'inseto', 'herbivoro', 'lagarta']

sanguessuga = ['invertebrado', 'anelideo', 'hematofago', 'sanguessuga']
minhoca = ['invertebrado', 'anelideo', 'onivoro', 'minhoca']

animais = [aguia, pomba, homem, vaca, pulga, lagarta, sanguessuga, minhoca]

animal_escolhido = []
for i in range(3):
    animal_escolhido.append(input())

for animal in animais:
    if animal[:3] == animal_escolhido:
        print(animal[3])
