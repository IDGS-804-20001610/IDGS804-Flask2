
from flask import Flask, render_template, request
import forms, caja_dinamica
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.config['SECRET_KEY']='esta es una clave encriptada'
csrf = CSRFProtect()

@app.route("/formPrueba")
def formprueba():
    return render_template("formprueba.html")

@app.route("/Alumnos", methods=['POST', 'GET'])
def Alumnos():
    reg_alum=forms.Userform(request.form)
    if request.method == 'POST':
        #obtenemos el contenido de la 'caja', gracias al .data
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("Alumno.html", form=reg_alum)

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

if __name__ == "__main__":
    #csrf.init_app(app)
    app.run(debug=True)