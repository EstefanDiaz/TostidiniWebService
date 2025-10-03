from flask import Flask, request, jsonify
import os 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    nombre = None
    if request.method == "POST":
        # Primero intentamos obtener desde formulario
        nombre = request.form.get("nombre")

        # Si no vino en form, probamos con JSON
        if not nombre and request.is_json:
            data = request.get_json()
            nombre = data.get("nombre")

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tostidini Web Service</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            tailwind.config = {{
                theme: {{
                    extend: {{
                        colors: {{
                            'tostidini-red': '#B91C1C',
                            'tostidini-orange': '#F59E0B',
                            'tostidini-bg': '#FFFBEB',
                        }},
                        fontFamily: {{
                            sans: ['Inter', 'sans-serif'],
                        }},
                    }}
                }}
            }}
        </script>
        <style>
            body {{
                font-family: 'Inter', sans-serif;
            }}
        </style>
    </head>
    <body class="bg-tostidini-bg min-h-screen flex items-center justify-center p-4">
        <div class="max-w-xl w-full bg-white shadow-2xl rounded-2xl p-8 md:p-10 text-center">

            <h1 class="text-4xl md:text-5xl font-extrabold text-tostidini-red mb-4">
                Bienvenido a Tostidini Web Servicini
            </h1>

            <div class="w-24 h-1 bg-tostidini-orange mx-auto my-6 rounded-full"></div>

            {"<h2 class='text-2xl font-bold text-tostidini-orange'>¡Hola, " + nombre + "!</h2>" if nombre else """
            <form method="POST" class="mt-4">
                <label class="block mb-2 text-gray-700 text-lg">Ingresa tu nombre:</label>
                <input type="text" name="nombre" required 
                    class="w-full p-2 border-2 border-tostidini-orange rounded-lg focus:outline-none focus:ring-2 focus:ring-tostidini-red">
                <button type="submit" 
                    class="mt-4 px-6 py-2 bg-tostidini-orange text-white font-semibold rounded-lg shadow-md hover:bg-tostidini-red transition">
                    Enviar
                </button>
            </form>
            """}

            <p class="text-md text-gray-500 mt-6">by Eva Estefani Diaz Beltrán<br>Matrícula: 22031466</p>
        </div>
    </body>
    </html>
    """

# Nueva ruta JSON
@app.route("/json", methods=["POST"])
def json_endpoint():
    if request.is_json:
        data = request.get_json()
        nombre = data.get("nombre", "invitado")
        return jsonify({
            "mensaje": f"¡Hola, {nombre}!",
            "estado": "éxito"
        })
    else:
        return jsonify({
            "error": "El body debe ser JSON con un campo 'nombre'"
        }), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask App running on http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port)
