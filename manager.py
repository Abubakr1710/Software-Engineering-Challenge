from flask import Flask,request,render_template,redirect,make_response,url_for,flash
 
from werkzeug.utils import secure_filename
 
import sqlite3
 
app = Flask(__name__)
  
@app.route("/", methods=['POST','GET'])
def upload():
    if request.method=="POST":    #need to remove
        destination_path="static/uploads"
        fileobj = request.files['file']
        file_extensions =  ["JPG","JPEG","PNG","GIF"]
        uploaded_file_extension = fileobj.filename.split(".")[1]
        
        if(uploaded_file_extension.upper() in file_extensions):
            destination_path= f"static/uploads/{fileobj.filename}"
            fileobj.save(destination_path)
            return '<h1>Uploaded</h1>'
        else:
            flash("only images are accepted")
    else:     
        return render_template('home.html') 