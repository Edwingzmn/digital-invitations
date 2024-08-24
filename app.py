from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def landing_page():
    # HTML template for the landing page
    html_content = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Invitaciones Digitales Personalizadas</title>
        <style>
            body {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                background-color: #f9f9f9;
                color: #333;
                margin: 0;
                padding: 0;
                text-align: center;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 40px 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            header h1 {
                font-size: 36px;
                margin: 0;
            }
            section {
                margin: 40px;
                padding: 40px;
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
            }
            h2 {
                font-size: 28px;
                color: #333;
                margin-bottom: 30px;
            }
            .package {
                border: 2px solid #4CAF50;
                border-radius: 8px;
                padding: 30px;
                margin: 30px 0;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .package:hover {
                transform: translateY(-10px);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            }
            .package h3 {
                font-size: 24px;
                color: #4CAF50;
                margin-bottom: 20px;
            }
            .package p {
                font-size: 18px;
                margin: 10px 0;
                color: #666;
            }
            .price {
                font-size: 26px;
                color: #4CAF50;
                margin-top: 20px;
                font-weight: bold;
            }
            footer {
                background-color: #333;
                color: white;
                padding: 20px;
                margin-top: 40px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Invitaciones Digitales Personalizadas para tus Eventos Especiales</h1>
        </header>
        <section>
            <h2>¡Haz que tu evento sea inolvidable desde el primer clic!</h2>
            
            <div class="package">
                <h3>Paquete Básico</h3>
                <p>Diseño elegante y personalizado</p>
                <p>Información del evento completa</p>
                <p>Envío digital fácil y rápido</p>
                <div class="price">$1000</div>
            </div>
            
            <div class="package">
                <h3>Paquete Avanzado</h3>
                <p>Todo lo incluido en el Paquete Básico</p>
                <p>Integración de enlaces RSVP para confirmar asistencia</p>
                <p>Galería de fotos del evento en tiempo real</p>
                <div class="price">$1500</div>
            </div>
            
            <div class="package">
                <h3>Paquete Premium</h3>
                <p>Todo lo incluido en el Paquete Avanzado</p>
                <p>Añade música de fondo para ambientar tu invitación</p>
                <p>Animaciones y efectos visuales para un impacto extra</p>
                <p>Asistencia técnica personalizada para asegurar que todo funcione a la perfección</p>
                <div class="price">$2000</div>
            </div>
            
            <h2>¡Transforma tu evento en una experiencia única desde la invitación!</h2>
        </section>
        <footer>
            <p>Contacta con nosotros para más información y empieza a sorprender a tus invitados hoy mismo.</p>
        </footer>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
