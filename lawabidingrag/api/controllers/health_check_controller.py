from flask import Blueprint

hc_bp = Blueprint('hc', __name__)

@hc_bp.route('/hc')
def health_check():
    return 'Im alive!'