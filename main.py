from flask import Flask, render_template_string
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)

bcrypt = Bcrypt(app)
api = Api(app)
CORS(app)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Live Clock</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 20%;
                }
                #clock {
                    font-size: 48px;
                    margin-bottom: 20px;
                    color: #FF4500;
                }
                #date {
                    font-size: 24px;
                    color: #FFD700;
                }
            </style>
        </head>
        <body>
            <div id="clock"></div>
            <div id="date"></div>
            <script>
                function updateTime() {
                    const now = new Date();
                    const hours = String(now.getHours()).padStart(2, '0');
                    const minutes = String(now.getMinutes()).padStart(2, '0');
                    const seconds = String(now.getSeconds()).padStart(2, '0');
                    const timeString = hours + ':' + minutes + ':' + seconds;

                    const year = now.getFullYear();
                    const month = String(now.getMonth() + 1).padStart(2, '0');
                    const day = String(now.getDate()).padStart(2, '0');
                    const dateString = year + '-' + month + '-' + day;

                    document.getElementById('clock').textContent = timeString;
                    document.getElementById('date').textContent = dateString;
                }

                setInterval(updateTime, 1000);
                updateTime(); 
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

    
