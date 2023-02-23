
#read
f = open('alumnos.txt','r')

'''alumnos = f.read()
print(alumnos)

# Para regresar a cierto caracter usamos el seek
f.seek(0)

alumnos2 = f.read()
print(alumnos2) 

alumno = f.readline()
print(alumno)

alumnos = f.readlines()
print(alumnos)
print(alumnos[0])

for item in alumnos:
    print(item, end = '')
f.close()
 
#write (si el archivo no existe, lo crea, WRITE solo reemplaza)
f = open('alumnos2.txt','w')
f.write('Hola Mundo')
f.write('Nuevo Hola Mundo')

#add (si el archivo no existe, lo crea, ADD lo agrega)
f = open('alumnos2.txt','a')
f.write('\n' + 'Hola Mundo')
f.write('\n' + 'Nuevo Hola Mundo')'''

f = open('alumnos.txt','r')
alumnos = []
alumnos1 = f.read()
alumnos2 = f.readline()
alumnos3 = f.readlines()

print(alumnos1)
#print(alumnos2)
#print(alumnos3)