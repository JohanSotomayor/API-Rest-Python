import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    os.environ['FLASK_APP'] = 'main.py'
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug=True)