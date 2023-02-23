
from flask import Flask, render_template, request, flash, make_response
import forms, caja_dinamica, traductor
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
            
    return render_template("traduccion.html", pa = pa, word = word)
    

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

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)