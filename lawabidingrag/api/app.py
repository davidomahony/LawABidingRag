from flask import Flask
from controllers.health_check_controller import hc_bp
from controllers.version_controller import info_bp
from controllers.query_controller import query_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(hc_bp)
app.register_blueprint(info_bp)
app.register_blueprint(query_bp)

if __name__ == '__main__':
    app.run(debug=True)