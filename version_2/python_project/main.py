from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template, session, redirect,url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'paystub'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ajbs1900",
  database="paystub"
)
print(mydb)

@app.route('/', methods=("POST", "GET"))
def home():
    mycursor = mydb.cursor()
    mycursor.excute("Select username,password,type From Employee")
    users = [dict((mycursor.discription[i][0],value)\
                for i,value in enumerate(row)) for row in mycursor.fetchall()]
    if request.method == 'POST':
        session.pop('user_id',None)
        username = request.form['username']
        password = request.form['password']
        type = request.form['type']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.employee_id
            if user.type == 'employee':
                return redirect(url_for('employee.html'))
            else:
                return redirect(url_for('manager.html'))
    return render_template('home.html', users=users)

@app.route('/Signin',methods=("POST","GET"))
def Signin():
    mycursor = mydb.cursor()
    mycursor.excute("")
    users = []
    return render_template('signin.html',users = users)

@app.route('/get_all_employee')
def get_employees():
    mycursor = mydb.cursor()
    mycursor.execute("Select * FROM Employee")
    r = [dict((mycursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in mycursor.fetchall()]
    # mycursor.connection.close()
    return (r[0])

if __name__ == '__main__':
    # get_employees()
    app.run(debug=True)
    