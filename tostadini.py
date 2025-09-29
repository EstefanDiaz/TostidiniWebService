from flask import Flask
import os

# Inicialización de la aplicación Flask
app = Flask(__name__)

@app.route("/")
def home():
    # El HTML incluye el CDN de Tailwind CSS y estilos para hacerlo estético y responsive.
    # Se usa una paleta de colores cálidos (naranja/rojo) con un fondo suave.
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tostidini Web Service</title>
        <!-- Carga del CDN de Tailwind CSS para estilos rápidos y responsivos -->
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            // Configuración de Tailwind para usar la fuente Inter y algunos colores
            tailwind.config = {
                theme: {
                    extend: {
                        colors: {
                            'tostidini-red': '#B91C1C', // Un rojo oscuro
                            'tostidini-orange': '#F59E0B', // Un naranja vibrante
                            'tostidini-bg': '#FFFBEB', // Amarillo muy claro para el fondo
                        },
                        fontFamily: {
                            sans: ['Inter', 'sans-serif'],
                        },
                    }
                }
            }
        </script>
        <style>
            /* Establece la fuente Inter y el fondo suave para toda la página */
            body {
                font-family: 'Inter', sans-serif;
            }
        </style>
    </head>
    <!-- Cuerpo de la página con fondo suave y centrado total -->
    <body class="bg-tostidini-bg min-h-screen flex items-center justify-center p-4">

        <!-- Contenedor principal de la tarjeta de bienvenida -->
        <div class="max-w-xl w-full bg-white shadow-2xl rounded-2xl p-8 md:p-10 text-center transform transition duration-500 hover:scale-[1.02]">
            
            <!-- Título principal con estilo dramático -->
            <h1 class="text-5xl md:text-6xl font-extrabold text-tostidini-red mb-4 tracking-tight leading-tight">
                Bienvenidos al 
                <span class="block text-tostidini-orange mt-1">TostidiniWebServicini</span>
            </h1>

            <!-- Línea separadora estética -->
            <div class="w-24 h-1 bg-tostidini-orange mx-auto my-6 rounded-full"></div>

            <!-- Subtítulo con información del autor -->
            <h2 class="text-lg md:text-xl font-medium text-gray-700">
                by Eva Estefani Diaz Beltrán
            </h2>
            <p class="text-md text-gray-500 mt-1">
                Matrícula: 22031466
            </p>

            <!-- Pequeño mensaje de ánimo -->
            <p class="mt-8 text-sm text-gray-400">
                ¡Servicio web corriendo con éxito!
            </p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    # Configuración para que Flask se ejecute en el puerto y host definidos por el entorno
    port = int(os.environ.get("PORT", 5000))
    print(f"Flask App running on http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port)
