from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Initialize the database
with app.app_context():
    db.create_all()

# index route that handles GET requests
@app.route('/')
def index():
    return "Hello, World!"

# route for registering users via a form
@app.route('/register', methods=['GET'])
def register():
    # Render a simple HTML form
    html_form = '''
        <h2>New user registration</h2>
        <form method="post" action="/user">
            Username: <input type="text" name="username"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Submit">
        </form>
    '''
    return render_template_string(html_form)

# route for creating a new user with POST requests
@app.route('/user', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"User {username} created successfully!"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
