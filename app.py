# from flask import Flask, render_template, redirect
# from forms import UploadForm
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'you-will-never-guess'
# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')

# @app.route('/',methods=['GET','POST'])
# def index():
# 	form = UploadForm()
# 	if form.validate_on_submit():
# 		print('submitted')
# 		return redirect('/uploaded_sucess')
# 	print(form.errors)
# 	return render_template('index.html',form=form)

# @app.route('/uploaded_sucess')
# def upload():
# 	return "Uploaded sucessfully"

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
import os
from flask import Flask, render_template,send_file
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField


basedir = os.path.abspath(os.path.dirname(__file__))

basepath = os.path.abspath(os.path.dirname(__file__))

image_path = basepath+"\\uploads\\"+'class1.jpg'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads') # you'll need to create a folder named uploads

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
	photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
	submit = SubmitField('Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
	form = UploadForm()
	if form.validate_on_submit():
		filename = photos.save(form.photo.data)
		file_url = photos.url(filename)
		

		
		if os.path.exists(image_path):
			os.remove(image_path)
		os.rename(basepath+"\\uploads\\"+filename,image_path)

		file_url = None
	else:
		file_url = None
	return render_template('index.html', form=form, file_url=file_url)

@app.route('/uploads/<classname>')
def send_images(classname):
	
	return send_file(basepath+"\\uploads\\"+classname)


if __name__ == '__main__':
	app.run()