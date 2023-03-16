
from flask import Flask, render_template, request, flash, make_response, redirect
import forms, caja_dinamica, traductor, resistencia, math, json
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.config['SECRET_KEY'] = "ESTA ES UNA LLAVE ENCRIPTADA"
csrf = CSRFProtect()

@app.route("/formPrueba")
def formprueba():
    return render_template("formprueba.html")

@app.route("/Alumnos", methods=['POST', 'GET'])
def Alumnos():
    reg_alum=forms.Userform(request.form)
    datos = list()
    if request.method == 'POST' and reg_alum.validate():
        #obtenemos el contenido de la 'caja', gracias al .data
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        #print(reg_alum.matricula.data)
        #print(reg_alum.nombre.data)
        print(datos[1])
    return render_template("Alumno.html", form=reg_alum, datos = datos)

@app.route("/numero", methods=['POST', 'GET'])
def cajaDinamica():
    numerocajas = request.form.get("txtNumCajas")
    numero = int(numerocajas or 0)
    n = int(numerocajas or 0)
    return render_template("caja_dinamica.html", numerocajas = numerocajas, numero = numero, n = n)

@app.route("/cajas", methods=['POST', 'GET'])
def cajaDinamicaRes():
    reg_caja = caja_dinamica.CajaForm(request.form)
    arreglo = [int(number or 0) for number in reg_caja.numeros.data]

    suma = 0
    total = len(arreglo)
    rep = {}

    for valor in arreglo:
        suma = suma + valor
        if valor in rep:
            rep[valor] += 1
        else: 
            rep[valor] = 1

    promedio = suma / total
    maximo = max(arreglo)
    minimo = min(arreglo)

    return render_template("caja_dinamica_resultado.html", maximo = maximo, minimo = minimo, promedio = promedio, rep=rep)

@app.route("/diccionario", methods = ['POST', 'GET'])
def palabras():
    reg_tra = traductor.traductor(request.form)
    datos = list()
    
    if request.method == 'POST' and reg_tra.validate():
        datos.append(reg_tra.espanol.data)
        datos.append(reg_tra.ingles.data)
        f = open('diccionario.txt', 'a')
        f.write(reg_tra.espanol.data.upper())
        f.write(' ' + reg_tra.ingles.data.upper() + '\n')

    return render_template("traductor.html", form = reg_tra)

@app.route("/traduccion", methods = ['POST', 'GET'])
def trad():
    lenguage = request.form.get("lenguage")
    pa = request.form.get("txtPalabra").upper()

    if request.method == 'POST':
        f2 = open('diccionario.txt', 'r')
        words = f2.read().splitlines()

        if lenguage == "2":
            word = [word.split(' ')[1] for word in words if word.split(' ')[0] == pa]
        else:
            word = [word.split(' ')[0] for word in words if word.split(' ')[1] == pa]

        if len(word) > 0:
            word1 = word[0]
            return ''' <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="../static/bootstrap/css/bootstrap.min.css">

    <title>Document</title>
    <style>
    </style>
    <link rel="stylesheet" href="../static/bootstrap/css/bootstrap-responsive.min.css">
</head>
<body>

<div class="container">
    <div clas="row">
        <h1>La traducción de la palabra "''' + pa + '''" es: '''+ word1 + '''</h1>
    </div>
</div>
</body>
</html>''' 
        else:
            word1 = "NO existe dentro de nuestro diccionario"
            
    return render_template("traduccion.html", pa = pa, word1 = word1)
    

@app.route("/cookie", methods = ['POST', 'GET'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookies.html', form = reg_user))

    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passsword = reg_user.password.data
        datos = user + '@' + passsword
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_usuario', datos)
        flash(success_message)
    return response

colores = ['negro', 'cafe', 'rojo', 'naranja', 'amarillo',
                'verde', 'azul', 'morado', 'gris', 'blanco']
color = ['oro', 'plata']

def calcular(bandas):
    resultado = float(f"{colores.index(bandas['ban1'])}{colores.index(bandas['ban2'])}") * float(f"1{colores.index(bandas['ban3']) * '0'}")
    minimo = resultado - (resultado * float(bandas['tolerancia']))
    maximo = resultado + (resultado * float(bandas['tolerancia']))

    return (
        bandas['ban1'],
        bandas['ban2'],
        bandas['ban3'],
        bandas['tolerancia'],
        resultado,
        minimo,
        maximo
    )
    

@app.route("/resistencia", methods = ['POST', 'GET'])
def resiste():

    reg_resis = resistencia.ResForm(request.form)

    datoss = list()

    filename = 'resistencia.json'
    
    with open(filename, 'r') as f:
        datos = json.load(f)

    data = [calcular(row) for row in datos] if datos != "" else False

    if request.method == 'POST' and reg_resis.validate():
        
        banda1 = request.form.get('banda1')
        banda2 = request.form.get('banda2')
        banda3 = request.form.get('banda3')
        tolerancia = request.form.get('tolerancia')

        ban1 = colores[int(banda1)]
        ban2 = colores[int(banda2)]
        ban3 = colores[len(banda3)-1]

        datoss.append(ban1)
        datoss.append(ban2)
        datoss.append(ban3)
        datoss.append(tolerancia)

        f = open('resistencia.txt', 'a')
        f.write(ban1.upper())
        f.write(' ' + ban2.upper())
        f.write(' ' + ban3.upper())
        f.write(' ' + tolerancia.upper() + '\n')

        jsonObj = {
            'ban1': colores[int(banda1)],
            'ban2': colores[int(banda2)],
            'ban3': colores[len(banda3) - 1],
            'tolerancia': tolerancia,
        }

        with open(filename, 'w') as f:
            json.dump([jsonObj, * datos], f)

        return redirect("/resistencia")
    
    return render_template("resistencia.html", form = reg_resis, datos = data)
'''
        valor = float(banda1 + banda2) * float(banda3)
        valorMin = valor - (valor * float(tolerancia))
        valorMax = valor + (valor * float(tolerancia))

        filename = 'resistencia.json'
        with open(filename, 'r') as f:
            datos = json.load(f)

        if isinstance(datos, list):
            datos.append({ 
            'valor:': str(valor),
            'min': str(valorMin),
            'max': str(valorMax), 
            'ban1': colors[int(banda1)], 
            'ban2': colors[int(banda2)], 
            'ban3': colors[len(banda3)-1], 
            })

        else:
            datos = [{ 
            'valor:': str(valor),
            'min': str(valorMin),
            'max': str(valorMax), 
            'ban1': colors[int(banda1)], 
            'ban2': colors[int(banda2)], 
            'ban3': colors[len(banda3)-1], 
            }]
            
        with open(filename, 'w') as f:
            json.dump(datos, f)

        #f = open('resistencia.txt', 'a')
        #f.write(f"{colors[int(banda1)]} {colors[int(banda2)]} {colors[len(banda3)-1]} {color[int(tolerancia)]}\n")
        # f.write('BANDA 2: ' + colors[int(banda2)] + '\n')
        #f.write('BANDA 3: ' + colors[len(banda3)-1] + '\n' + '\n')
        # f.write('BANDA 3: ' + colors[len(banda3)-1] + '\n' + '\n')
    
        
        datos = [{ 
            'RESULTADO:': str(valor),
            'MINIMO': str(valorMin),
            'MAXIMO': str(valorMax), 
            'ban1': colors[int(banda1)], 
            'ban2': colors[int(banda2)], 
            'ban3': colors[len(banda3)-1], 
            }]
    else:
        with open('resistencia.txt', 'r') as file:
            lines = file.read().splitlines()
            [line.split(' ') for line in lines]

        
    return render_template("resistencia.html",form=reg_resis, datos = datos)

'''
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)