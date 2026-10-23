Numeros = [5,7,8,10,12,18,20,25,30,35,40,48,5,20,40]

Mayor=0
Smayor=0

for numero in Numeros:
  if numero > Mayor:
    Smayor = Mayor
    Mayor = numero
  else:
    if numero != Mayor:
      if numero > Mayor:
        Smayor =Mayor
if Smayor == 0:
  print('no existe un numero igual')
else:
  print('el mayor es:',Mayor)
  print('El segundo Mayor es:',Smayor)
  print('la diferencias de numeros es:', Mayor-Smayor)