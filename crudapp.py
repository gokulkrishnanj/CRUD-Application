from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL
crudapp=Flask(__name__)
crudapp.config["MYSQL_HOST"]="localhost"
crudapp.config["MYSQL_USER"]="root"
crudapp.config["MYSQL_PASSWORD"]="root"
crudapp.config["MYSQL_DB"]="crudapplication"
crudapp.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(crudapp)

@crudapp.route("/")
def home():
    con=mysql.connection.cursor()
    sql="select * from users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("flask.html",datas=res)
@crudapp.route("/addname",methods=['GET','POST'])
def addname():
    if request.method=='POST':
        name=request.form['name']
        city=request.form['city']
        age=request.form['age']
        con=mysql.connection.cursor()
        sql="insert into users (NAME,CITY,AGE) value (%s,%s,%s)"
        con.execute(sql,[name,city,age])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("addname.html")
@crudapp.route("/editname/<string:id>",methods=['GET','POST'])
def editname(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        city=request.form['city']
        age=request.form['age']
        sql="update users set NAME=%s,CITY=%s,AGE=%s where ID=%s"
        con.execute(sql,[name,city,age,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editname.html",datas=res)
@crudapp.route("/deletename/<string:id>",methods=['GET','POST'])
def deletename(id):
    con=mysql.connection.cursor()
    sql="delete from users where ID=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))
if(__name__=='__main__'):
    crudapp.run(debug=True)