# import flask
# from flask import Flask, render_template, request, flash, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     name = db.Column(db.String(120), nullable=False)
#     phone = db.Column(db.String(20), nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'

# @app.route('/contact', methods=['POST'])
# def register():
#     username = request.form.get('username')
#     email = request.form.get('email')
#     name = request.form.get('name')
#     phone = request.form.get('phone')

#     # Create a new user instance
#     new_user = User(username=username, email=email, name=name, phone=phone)

#     # Add the new user to the database session
#     db.session.add(new_user)

#     # Commit the session to save the changes
#     db.session.commit()

#     # Flash a success message
#     flash('Thank you for registering!')

#     # Redirect to a thank-you page or the home page
#     return redirect(url_for('thank_you'))

# @app.route('/thank_you')
# def thank_you():
#     return render_template('about.html')

# if __name__ == '__main__':
#     # Create the database tables before running the app
#     db.create_all()
#     app.run(debug=True)
