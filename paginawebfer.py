from flask import Flask,render_template
#import mysql.connector
import psycopg2
#import os
#import sys
#from string import Template
#aqui la conexion de python a html
#filein = open('templates/layot.html')
#src=Template(filein.read())

#conexión a base de datos 
mydb = psycopg2.connect(
    host='ec2-52-3-200-138.compute-1.amazonaws.com',
    user='fdecjtyvkswfhn',
    port='5432',
    password='503e14b5b87fe81ccc7de48bcc5979402c471f46798851733e69f1d2bbed3abf',
    database='dabtou06s1ljtc'
    )
print (mydb)
#esto solo nos imprime si la conexión se hizo
cursor = mydb.cursor()



#datos = cursor.fetchall()
#for fila in datos:
#    print(fila)
#result = src.substitute(Nombre)



app=Flask(__name__)
print("aqui entra a home")
@app.route('/')
def home():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    print("Propietario de la página es: "+ Cliente[1])
    return render_template('home.html',Cliente=Cliente)

@app.route('/about')
def about():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    return render_template('about.html',Cliente=Cliente)

def layout():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    print(Cliente[3])
    return render_template('layout.html',Cliente=Cliente)

@app.route('/fisica')
def fisica():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    return render_template('fisica.html',Cliente=Cliente)


@app.route('/matematicas')
def matematicas():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    return render_template('matematicas.html',Cliente=Cliente)    

@app.route('/programacion')
def programacion():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    return render_template('programacion.html',Cliente=Cliente)

if __name__ =='__main__':
    app.run()
    #debug=True  esto dentro del run 
#esto hace que agarre sus cambios cuando esta en desarrollo 

mydb.close()
print("conexión a base de datos cerrada")
    
