from unicodedata import name
from flask import Flask, render_template, url_for, request, redirect
import sqlite3
import os


app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
         #data = request.form.to_dict()
         #print(data)
         email= request.form["email"]
         subject=request.form["subject"]
         message=request.form["message"]
         connection=sqlite3.connect("sqlite_contact.db")
         cursor= connection.cursor()
         query1= "INSERT INTO contactus VALUES('{email}','{subject}','{message}')".format(email=email,subject=subject,message=message) 
         cursor.execute(query1)
         connection.commit()
         return redirect('/thankyou.html')
        except:
            return "Some problem occured, try to submit form again."
    else:
        return "something went wrong. Try Again"




