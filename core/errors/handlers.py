from flask import Blueprint, render_template
from core.models import db

error_blueprint = Blueprint('errors', __name__)

@error_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@error_blueprint.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500