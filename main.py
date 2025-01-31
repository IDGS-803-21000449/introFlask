

from flask import Flask, render_template, request

app = Flask(__name__)  

@app.route('/')
def index():
    grupo="IDGS803"
    lista=["Juan", "Pedro", "Maria"]
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route("/OperaBas")
def operas():
    return render_template("OperaBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

    return "La suma de {} y {} es: {} ".format(num1, num2, int(num1)+ int(num2))


@app.route('/cal', methods=['GET', 'POST'])
def calcular():

    resultado = ""

    if request.method == 'POST':
        n1 = int(request.form.get('n1', 0))
        n2 = int(request.form.get('n2', 0))
        resultado = str(n1 + n2)

    return render_template("OperaBas.html", resultado=resultado)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "Hola!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} id: {id}!!!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es {}!!!".format(n1 + n2)


if __name__ == "__main__":
    app.run(debug=True)

    