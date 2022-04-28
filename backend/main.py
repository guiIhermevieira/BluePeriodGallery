from curses import flash
import os
from flask import Flask, render_template, request, redirect, send_file, jsonify
from flask_cors import CORS
from s3_functions import upload_file, show_image
from werkzeug.utils import secure_filename
import uuid
from flask_login import login_user, LoginManager, login_required, current_user
from flask_wtf import FlaskForm
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash 

mongo = PyMongo()

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "blue-period-art-gallery"

app.config['MONGO_URI'] = 'mongodb+srv://yorick:<password>@cluster0.6bzs1.mongodb.net/mydb?retryWrites=true&w=majority'

mongo.init_app(app)


app.config.from_object(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


ART_WORKS = [

  {
    "title": "The Blue Period",
    "artist": "Van Gogh",
    "year": "1889",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Van_Gogh_-_The_Blue_Period_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_The_Blue_Period_-_Google_Art_Project.jpg",
    "description": "The Blue Period is a painting by Dutch post-impressionist painter Vincent van Gogh. It was painted in June 1889 and was sold for $1,500 at the Sotheby's auction house in New York City. The painting is in the collection of the Museum of Modern Art in New York City.",
    "status": "sold",
    "sold_to": "Sotheby's",
    "materials_used": "Oil on canvas",
    "active": True
  }
]


CORS(app, resources={r"/*":{'origins': "*"}})

@app.route('/admin')
@login_required
def admin():
  id = current_user.id
  if id == 1:
    return render_template('admin.html')
  else:
    flash('You are not authorized to view this page')
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login(): 
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user: 
      if check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        return redirect(url_for('admin'))
      else: flash('Incorrect password')
    else: flash('Username does not exist')
  return render_template('login.html', form=form)

@app.route('/', methods=['GET'])
def greetings(): 
  return ("Hello World")

@app.route('/arts', methods=['GET'])
def all_arts():
  return jsonify({
    'artworks': ART_WORKS,
    'status': 'success'
  })

@app.route('/submit', methods=['POST'])
def submit_art():
  response_object = {'status': 'success'}
  if request.method == "POST":
    post_data = request.get_json()
    ART_WORKS.append({
      'id': uuid.uuid4().hex,
      'title': post_data['title'],
      'artist': post_data['artist'],
      'year': post_data['year'],
      'image': post_data['image'],
      'description': post_data['description'],
      'status': post_data['status'],
      'sold_to': post_data['sold_to'],
      'materials_used': post_data['materials_used'],
      'active': False 
      })
    response_object['message'] = 'Artwork added!'
  else: 
    response_object['art_works'] = ART_WORKS
  return jsonify(response_object)

@app.route('/submissions', methods=['GET', 'POST'])
def submission():
  response_object = {'status': 'success', 'data': ART_WORKS}
  if request.method == 'POST':
    post_data = request.get_json()
    ART_WORKS.append({
      'id': uuid.uuid4().hex,
      "title": post_data('title'),
      "artist": post_data('artist'),
      "year": post_data('year'),
      "image": post_data('image'),
      "description": post_data('description'),
      "expected_price": post_data('expected_price'),
      "status": post_data('status'),
      "sold_to": post_data('sold_to'),
      "materials_used": post_data('materials_used'),
      "active": True
    })
  else: 
    response_object['art_works'] = ART_WORKS
  return jsonify(response_object)


@app.route("/upload", methods=['POST'])
def upload():
  if request.method == "POST":
    f = request.files['file']
    f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
    upload_file(f"uploads/{f.filename}", BUCKET)
    return redirect("/")


@app.route("/show", methods=['GET'])
def list():
  contents = show_image(BUCKET)
  return render_template("list.html", contents=contents)



if __name__ == "__main__":
  app.run(debug=True)