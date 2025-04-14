from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from presentation_layer.routes.contacts_routes import contact_bp


def create_app():
    app = OpenAPI(
        __name__,
        info=Info(title="Contact API", version="1.0.0"),
        doc_ui='swagger',  # garante que o Swagger seja carregado
    )

    CORS(app)
    app.register_api(contact_bp, url_prefix="/api")
    return app
