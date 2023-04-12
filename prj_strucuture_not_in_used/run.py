from app import create_app
from app.routes import api_blueprint

app = create_app()

if __name__ == '__main__':
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.run()