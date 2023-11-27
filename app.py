from flask import Flask
from flask_login import LoginManager, login_required
from website.models import db, load_user
from website.routes import home, login, dashboard, logout, register


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SECRET_KEY'] = 'your-secret-key'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.user_loader(load_user)

app.route("/")(home)
app.route("/login", methods=["GET", "POST"])(login)
app.route("/dashboard", methods=["GET", "POST"])(login_required(dashboard))
app.route("/logout", methods=["GET", "POST"])(login_required(logout))
app.route("/register", methods=["GET", "POST"])(register)


if __name__ == "__main__":
    with app.app_context():  
        db.create_all()
    app.run(debug=True)