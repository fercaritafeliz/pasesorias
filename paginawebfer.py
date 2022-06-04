#escencial para que se hagan las paginas
from pyexpat import model
from flask import Flask,render_template, request, send_from_directory
import os
import psycopg2
#---------------------------------------------------------------------------
#import sys
#from string import Template
#import mysql.connector
#aqui la conexion de python a html
#filein = open('templates/layot.html')
#src=Template(filein.read())
#---------------------------------------------------------------------------
#conexión a base de datos mysql
#---------------------------------------------------------------------------
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import numpy as np
#import seaborn as sns
#---------------------------------------------------------------------------
#cosas para graficar
#---------------------------------------------------------------------------
#datos = cursor.fetchall()
#for fila in datos:
#    print(fila)
#result = src.substitute(Nombre)
#cosas para leer lo que hy en la base de datos
#---------------------------------------------------------------------------

app=Flask(__name__)
#conexión de base de datos de postgres
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
#cursor es para ejecutar codigo de SQL
print("aqui entra a home")
@app.route('/', methods=['GET', 'POST'])
def home():
    x1 =0.01
    x2 =6
    k=0
    x=np.linspace(-1,6,100)
    def f(x):
        return (x/5)+(1/np.exp(x))-1
    while k<100:
        x1=x1-(((x1/5)+(1/(np.exp(x1))-1))/((1/5)-(np.exp(-x1))))
        z1=f(x1)
        print("valor x1:"+str(x1)+"valor f(x1):"+str(z1))
        plt.scatter(x1,f(x1))
        x2=x2-(((x2/5)+(1/(np.exp(x2))-1))/((1/5)-(np.exp(-x2))))
        z=f(x2)
        print("valor x2:"+str(x2)+"valor f(x2):"+str(z))  
        plt.scatter(x2,f(x2))
        k=k+1
    
    #plt.clf() 
    img = io.BytesIO()
    plt.title("Método Newton-Raphson")
    plt.xlabel('Unidades en x')
    plt.ylabel('Unidades en f(x)')
    plt.plot(x,f(x))
    plt.grid()
    plt.savefig(img, format='png')
    plt.switch_backend('agg')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    print("Propietario de la página es: "+ Cliente[1])
    if request.method == 'POST':
        model.save()
        # Failure to return a redirect or render_template
    else:
        return render_template('home.html',Cliente=Cliente,imagen={ 'imagen': plot_url })
    
    
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon.ico',mimetype='./images/favicon.ico')

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

@app.route('/Electrospinning')
def Electrospinning():
    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
    Cliente = cursor.fetchone()
    return render_template('Electrospinning.html',Cliente=Cliente)


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



#@app.route('/grafica')
#def grafica():
#    x=[1,2,3]
#    y=[1,2,3]
#    cursor.execute("SELECT * FROM clietes WHERE ID = 1")
#    Cliente = cursor.fetchone()
    #plt.clf() 
#    img = io.BytesIO()
#    plt.title("la grafica por: ")
#    plt.plot(x,y)
#    plt.savefig(img, format='png')
#    plt.switch_backend('agg')
#    img.seek(0)
#    plot_url = base64.b64encode(img.getvalue()).decode()
#    return render_template('grafica.html', imagen={ 'imagen': plot_url },Cliente=Cliente)



if __name__ =='__main__':
    app.run(debug=True)
#esto hace que agarre sus cambios cuando esta en desarrollo 
#debug=True






#mydb.close()
#print("conexión a base de datos cerrada")


