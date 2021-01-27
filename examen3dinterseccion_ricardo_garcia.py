"""
Examen de interseccion 3D
Graficacion
Ricardo Gabriel Garcia Gomez 
Num  control 18390026
"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import tools3d 

#______Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
x=[-40,-40,40,-5,5]
y=[0,0,0,-20,10]
z=[-10,10,10,0,0]

for i in range(len(x)):
    xg.append(x[i]+xc)
    yg.append(y[i]+yc)
    zg.append(z[i]+zc)

#____Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
#1def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,validohit,A,A1,A2):
    #tamaño de la ventana
    plt.axis([0,120,0,100])
    plt.axis('on')
    plt.grid(False)
    #triangulo
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')

    #triangulos extras
    plt.plot([xg[0],xg[4]],[yg[0],yg[4]],color='r')
    plt.plot([xg[4],xg[1]],[yg[4],yg[1]],color='r')
    plt.plot([xg[4],xg[2]],[yg[4],yg[2]],color='r')

    #linea de interseccion
    plt.plot([xg[3],xg[4]],[yg[3],yg[4]],color='b')#Line

   
    if(validohit==True):
        plt.text(20,20,'Esta dentro del plano')
    else:
        plt.text(20,20,'Fuera del plano')

    plt.text(10,60,'Ricardo Gabriel Garcia Gomez')
    plt.text(10,40,'A=')
    plt.text(14,40,A)
    plt.text(10,35,'A1=')
    plt.text(16,35,A1)
    plt.text(10,30,'A2=')
    plt.text(16,30,A2)
    plt.text(10,25,'A1+A2=')
    plt.text(25,25,A1+A2)


    plt.show()

def hitpoint(x,y,z):
    #distancia de 0 a 1
    a=x[0]-x[1]
    b=y[0]-y[1]
    c=z[0]-z[1]
    d01=sqrt(a*a+b*b+c*c) 
    #distancia de 1 a 2
    a=x[1]-x[2]
    b=y[1]-y[2]
    c=z[1]-z[2]
    d12=sqrt(a*a+b*b+c*c) 
    #distancia de 2 a 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    d20=sqrt(a*a+b*b+c*c) 

    #calcular Area A
    s=(d01+d12+d20)/2
    A=sqrt(s*(s-d01)*(s-d12)*(s-d20))

    #distancia de 0 a 1
    a=x[0]-x[1]
    b=y[0]-y[1]
    c=z[0]-z[1]
    d01=sqrt(a*a+b*b+c*c) 
    #distancia de 1 a hit
    a=x[1]-x[3]
    b=y[1]-y[3]
    c=z[1]-z[3]
    d13=sqrt(a*a+b*b+c*c) 
    #distancia de hit a 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    d30=sqrt(a*a+b*b+c*c) 

    #calcular Area A1
    s=(d01+d13+d30)/2
    A1=sqrt(s*(s-d01)*(s-d13)*(s-d30))

    #distancia de 0 a 2
    a=x[0]-x[2]
    b=y[0]-y[2]
    c=z[0]-z[2]
    d02=sqrt(a*a+b*b+c*c) 
    #distancia de 2 a hit
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    d23=sqrt(a*a+b*b+c*c) 
    #distancia de hit a 0
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    d30=sqrt(a*a+b*b+c*c) 

    #calcular Area A2
    s=(d02+d23+d30)/2
    A2=sqrt(s*(s-d02)*(s-d23)*(s-d30))

    #calcula si el hitpoint esta dentro o fuera
    sumaarea=A1+A2
    validohit=True
    if(sumaarea<A):
        validohit=True
    else:
        validohit=False
    #convertir los float en int
    A=int(A)
    A1=int(A1)
    A2=int(A2)

    #mandar al plot los valores
    plotPlaneLine(xg,yg,zg,validohit,A,A1,A2)
 



def plotPlaneLinex(xc,yc,zc,Rx,hitx1,hity1,hitx2,hity2):
    for i in range(len(y)):
        x[3]=int(hitx1)
        y[3]=int(hity1)
        x[4]=int(hitx2)
        y[4]=int(hity2)
        [xg[i],yg[i],zg[i]]=tools3d.rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    
    hitpoint(x,y,z)
    
    

def plotPlaneLiney(xc,yc,zc,Ry,hitx1,hity1,hitx2,hity2):
    for i in range(len(y)):
        x[3]=int(hitx1)
        y[3]=int(hity1)
        x[4]=int(hitx2)
        y[4]=int(hity2)
        [xg[i],yg[i],zg[i]]=tools3d.rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    
    hitpoint(x,y,z)
    

def plotPlaneLinez(xc,yc,zc,Rz,hitx1,hity1,hitx2,hity2):
    for i in range(len(y)):
        x[3]=int(hitx1)
        y[3]=int(hity1)
        x[4]=int(hitx2)
        y[4]=int(hity2)
        [xg[i],yg[i],zg[i]]=tools3d.rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)
        [x[i],y[i],z[i]]=[xg[i]-xc,yg[i]-yc,zg[i]-zc]
    hitpoint(x,y,z)
    
    

####_____pedir al usaurio que eje desea trabajar y plotear el PlaneLine
#insertar el hitpoint
while True:
    hitx1=input("Teclea el hitpoint x1 ?:")
    hity1=input("Teclea el hitpoint y1 ?:")
    hitx2=input("Teclea el hitpoint x2 ?:")
    hity2=input("Teclea el hitpoint y2 ?:")
    axis=input("Teclea el eje que deseas visualizar 'x,y,z' o pulsa el num control para salir ?:")
    if axis=='x':#plotear el eje X
        Rx=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinex(xc,yc,zc,Rx,hitx1,hity1,hitx2,hity2)#LLamamos a la funcion de ploteo
    if axis=='y':
        Ry=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLiney(xc,yc,zc,Ry,hitx1,hity1,hitx2,hity2)#LLamamos a la funcion de ploteo
    if axis=='z':
        Rz=radians(float(input('Dame los grados de rotacion ?: ')))
        plotPlaneLinez(xc,yc,zc,Rz,hitx1,hity1,hitx2,hity2)#LLamamos a la funcion de ploteo
    if axis== '18390026':
        break