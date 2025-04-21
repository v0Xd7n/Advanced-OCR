import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'bmp', 'gif'}
app.config['THUMBNAIL_SIZE'] = (300, 300)  # Preview image dimensions

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_thumbnail(image_path):
    try:
        with Image.open(image_path) as img:
            img.thumbnail(app.config['THUMBNAIL_SIZE'])
            thumb_path = os.path.join(app.config['UPLOAD_FOLDER'], 'thumb_' + os.path.basename(image_path))
            img.save(thumb_path)
            return thumb_path
    except Exception as e:
        print(f"Thumbnail creation failed: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            try:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Create thumbnail
                thumb_path = create_thumbnail(filepath)
                
                lang = request.form.get('lang', 'eng')
                psm = request.form.get('psm', '6' if lang == 'hin' else '3')
                
                text = pytesseract.image_to_string(
                    Image.open(filepath),
                    lang=lang,
                    config=f'--psm {psm} --oem 1'
                ).strip()
                
                if not text:
                    text = "No text could be extracted from the image."
                    flash('No text found in image', 'warning')
                
                return render_template('result.html', 
                                    text=text, 
                                    image_path=filepath,
                                    thumb_path=thumb_path,
                                    lang=lang,
                                    psm=psm)
            
            except Exception as e:
                flash(f'Error processing image: {str(e)}', 'error')
                return redirect(request.url)
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)