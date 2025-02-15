from flask import render_template
from flask import Blueprint , request, redirect, url_for
from app.models.user_models import User
from app.models import db
users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/' , methods=['GET'])
def show_users():
    users=User.query.all()
    return(render_template('user/list.html', users=users))

@users_bp.route('/create' , methods=['GET'])
def user_signup():
    return render_template('user/edit.html')

@users_bp.route('/create' , methods=['POST'])
def create_user():
    data = request.form
    print("request=",request)
    print("data=",data)
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    user = User(
        name=name,
        email=email,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return (redirect(url_for('users.show_users')))