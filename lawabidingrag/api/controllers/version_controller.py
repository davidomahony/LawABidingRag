from flask import Blueprint

info_bp = Blueprint('info', __name__)

@info_bp.route('/info')
def version_info():
    return 'Hello, World!'