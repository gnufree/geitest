#!/usr/bin/python

from flask import Flask,request,render_template,flash,redirect
import random
import MySQLdb

app = Flask(__name__)
app.secret_key = '#$%seruu%$#'

@app.route('/inner',methods=['GET','POST'])
def inner():
    if request.method == 'GET':
        return render_template('inner.html')
    elif request.method == 'POST':
        email = request.form['email']
        invite_code = ''.join(random.sample('1234567890abcdefghjklmnopqrstuvwxyz()',4))
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='mysite')
        cursor = conn.cursor()
        if email == '':
            flash('Please enter a valid content')
            return render_template('inner.html')
        cursor.execute("select count(email) from tbl_inner where email=%s",email)
        result = cursor.fetchone()
        if result[0] == 0:
            sql = 'insert into tbl_inner(email,invite_code)values(%s,%s)'
            cursor.execute(sql,(email,invite_code))
            conn.commit()
            #flash('Register successfully')
            return redirect('/regist')
        else:
            flash('Email has been registered, please try a different email')
        cursor.close()
        conn.close()
    return render_template('inner.html')

@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    elif request.method == 'POST':
        email = request.form['email']
        passwd = request.form['password']
        invite_code = request.form['invite_code']
        if 

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

