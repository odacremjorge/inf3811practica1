from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return ("Bienvenidos esta es la practica 1 de Jorge Alejandro mercado Araya")
@app.route("/saludo")
def saludo():
    return ("Realizando nuevas rutas")   
if __name__ == "__main__":
    app.run(debug=True, port=5001)