from flask import render_template
from flask import Blueprint
users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/create' , methods=['GET'])
def user_signup():
    return render_template('user/edit.html')