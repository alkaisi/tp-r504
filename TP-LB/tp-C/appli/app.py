# TP_LB/tp-C/appli/app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    container_id = os.environ.get('HOSTNAME', 'Unknown')
    return f'Serveur dans le conteneur {container_id}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
