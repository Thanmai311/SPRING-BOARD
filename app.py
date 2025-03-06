from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    father_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    number = db.Column(db.String(15), unique=True, nullable=False)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Register Route
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    father_name = request.form['f_name']
    email = request.form['email']
    number = request.form['number']

    if User.query.filter_by(email=email).first():
        flash('Email already registered! Try another.', 'danger')
        return redirect(url_for('home'))
    
    new_user = User(name=name, father_name=father_name, email=email, number=number)
    db.session.add(new_user)
    db.session.commit()

    flash('Registration successful!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    print("Starting Flask application...")
    with app.app_context():
        print("Creating database tables if they don't exist...")
        db.create_all()
    print("Running Flask app...")
    app.run(debug=True)
