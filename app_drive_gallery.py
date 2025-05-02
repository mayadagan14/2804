
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def gallery():
    images = [
        "https://drive.google.com/uc?export=view&id=1-ThUMp6vxPoOgEYEKA-XPDENhuZWaxxd",
        "https://drive.google.com/uc?export=view&id=1-_6Ncj9AlKH8S2DV0umYPsfUAVsvfscV",
        "https://drive.google.com/uc?export=view&id=102sGRyTRJc3ah4g7a7QQ3e7uVsXnECm-",
        "https://drive.google.com/uc?export=view&id=10uspi2S7c8Suwu-t9JVHLd010W3aSjlw",
        "https://drive.google.com/uc?export=view&id=114IArBelye2WLMqGtGVbwVTieUhKWjCF"
    ]

    html = """
    <!DOCTYPE html>
    <html lang="he">
    <head>
        <meta charset="UTF-8">
        <title>גלריה – החתונה של מאיה וסתיו</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #fdf7f2;
                margin: 0;
                padding: 0;
                text-align: center;
            }
            h1 {
                background-color: #dec8ae;
                color: #7a3e3e;
                padding: 20px;
                margin: 0;
            }
            .gallery {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 16px;
                padding: 20px;
            }
            .gallery-item {
                position: relative;
                overflow: hidden;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .gallery-item img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: transform 0.3s ease;
            }
            .gallery-item:hover img {
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <h1>💍 החתונה של מאיה וסתיו – 28.04.2025 💍</h1>
        <div class="gallery">
            {% for url in images %}
            <div class="gallery-item">
                <img src="{{ url }}" alt="תמונה מהחתונה">
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, images=images)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=10000)

