from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Santi! Tu API Flask está funcionando ✅"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre", "amigo")
    return jsonify({"saludo": f"Hola, {nombre}! Esto es Flask en Render 🚀"})

if __name__ == "__main__":
    app.run()
