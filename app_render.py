
from flask import Flask, render_template_string
import os

app = Flask(__name__)

# תמונות מ-Google Drive
images = [
    "https://drive.google.com/uc?export=view&id=1AnR80Wsjq02MggOpSj6jVX22Ev8RYSiB",
    "https://drive.google.com/uc?export=view&id=15g2FE1XBp4d-dx_kOcBf5uPZzqeDowDX",
    "https://drive.google.com/uc?export=view&id=102sGRyTRJc3ah4g7a7QQ3e7uVsXnECm-",
    "https://drive.google.com/uc?export=view&id=1vwDeQXeG-c_nTiWC9NSAO_QsXQ5RHWg_",
    "https://drive.google.com/uc?export=view&id=1I8ClpAVQ0-1-RZoOZKAm9J1VMt7b4VSK",
    "https://drive.google.com/uc?export=view&id=1-ThUMp6vxPoOgEYEKA-XPDENhuZWaxxd"
]

@app.route('/')
def gallery():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="he">
    <head>
        <meta charset="UTF-8">
        <title>החתונה של מאיה וסתיו</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #fdf7f2;
                text-align: center;
                direction: rtl;
            }
            h1 {
                background-color: #dec8ae;
                color: #7a3e3e;
                padding: 20px;
            }
            .gallery {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                padding: 20px;
            }
            .gallery img {
                width: 100%;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <h1>💍 החתונה של מאיה וסתיו – 28.04.2025 💍</h1>
        <div class="gallery">
            {% for img in images %}
            <div><img src="{{ img }}" alt="תמונה מהחתונה"></div>
            {% endfor %}
        </div>
    </body>
    </html>
    """, images=images)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
