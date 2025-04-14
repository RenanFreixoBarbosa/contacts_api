from presentation_layer.routes.contacts_routes import contact_bp
from presentation_layer.config.swagger_config import create_app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)