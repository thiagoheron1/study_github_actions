"""Factory da Aplicação Web."""
from flask import Flask

def create_app():
    """Constroi a aplicação."""
    app = Flask(__name__)

    app.get("/soma/<int:x>/<int:y>")
    def home(x, y):
        # return str(soma(x, y))
        return f'blah {x} e {y}'
    return app