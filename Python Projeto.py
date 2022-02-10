import numpy as np
numeros = np.array ([2,4,6,8,10])

print (numeros)

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('maior: ',maior)

  
menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro

print('menor: ',menor)

media = primeiro

if (segundo % media):
        media = segundo
if (terceiro % media):
        media = terceiro

print ('media:  ', media)