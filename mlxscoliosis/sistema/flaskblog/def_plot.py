import os

from scipy.ndimage import rotate
from scipy.misc import imread, imshow
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate
import cv2
import imutils
from operator import is_not
from functools import partial
from pylab import *
from random import *
from sklearn.cluster import KMeans
from matplotlib import transforms
import scipy.ndimage.morphology as morp
from skimage import feature
from flaskblog.defs import *
import math

def img_plot(x_new2,y_new,file_name,fig,ax,a_2,b_2,aaa,bbb):
    ruta = 'flaskblog/static/'+file_name
    imagen2 = cv2.imread(ruta, cv2.IMREAD_COLOR)
    img2 = rotate(imagen2, -90)

    dimensions = imagen2.shape
    height = imagen2.shape[0]
    width = imagen2.shape[1]
    ancho = int(width)
    altura = int(height)
    width = altura

    height = ancho
    dim = (width, height)
    resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

    aa = ax.imshow(resized)

    altura = imagen2.shape[0]
    width = imagen2.shape[1]
    #y_grafo = y

    #y_inv = y[::-1]
    inflex_x=aaa
    inflex_y=bbb
    print("esto es lo q llego de pi1",inflex_x)
    print("esto es lo q llego de pi2",inflex_y)
    point_x=a_2
    
    #point_y =[x-200 for x in b_2]
    point_y=b_2
    print("coordenadas en POINT X:",point_x)
    print("coordenadas en POINT Y:",point_y)

    tam_point=len(point_x)
    enl_x1=[]
    enl_y1=[]
    enl_x1.append(inflex_x[0])
    enl_y1.append(inflex_y[0])
    enl_x2=[]
    enl_y2=[]
    enl_x2.append(inflex_x[1])
    enl_y2.append(inflex_y[1])

    enl_x3=[]
    enl_y3=[]
    enl_x3.append(inflex_x[1])
    enl_y3.append(inflex_y[1])
    enl_x4=[]
    enl_y4=[]
    enl_x4.append(inflex_x[2])
    enl_y4.append(inflex_y[2])


	#point_x=[1000, 678.18396024]
	#point_y=[500, 154.11426059173402]
    enl_x1.append(point_x[1])
    enl_y1.append(point_y[1])
    enl_x2.append(point_x[1])
    enl_y2.append(point_y[1])

    enl_x3.append(point_x[0])
    enl_y3.append(point_y[0])
    enl_x4.append(point_x[0])
    enl_y4.append(point_y[0])

    point_x1=point_x[0]
    point_x2=point_x[1]
    plt.plot(inflex_x, inflex_y, marker = 'o')
    plt.plot(point_x1,point_x2, marker = 'o',color='red')
    point_prueba1=[955,313]
    point_prueba2=[403,237]
    plt.plot(enl_x1,enl_y1, marker = 'o')
    plt.plot(enl_x2,enl_y2, marker = 'o')

    plt.plot(enl_x3,enl_y3, marker = 'o',color='red')
    plt.plot(enl_x4,enl_y4, marker = 'o',color='red')
    point_prueba3=[583,313]
    point_prueba4=[385,237]
	#plt.plot(point_prueba3,point_prueba4, marker = 'o')

	
    #calculo de c
    x1=inflex_x[0]
    y1=inflex_y[0]
    #print("EQUIS 1",x1)
    #print("YE 1",y1)
    x2=inflex_x[1]
    y2=inflex_y[1]
    #print("EQUIS 2",x2)
    #print("YE 2",y2)
    sum1=((x2-x1)**2)+((y2-y1)**2)
    
    c=sum1**0.5
    
    print("c",c)

    #calculo de a
    x3=inflex_x[0]
    y3=inflex_y[0]
    x4=point_x[1]
    y4=point_y[1]
    sum2=((x4-x3)**2)+((y4-y3)**2)

    a=sum2**0.5
    print("a",a)


    #calculo de b
    x5=inflex_x[1]
    y5=inflex_y[1]
    x6=point_x[1]
    y6=point_y[1]
    sum3=((x6-x5)**2)+((y6-y5)**2)

    b=sum3**0.5
    print("b",b)


    #calculo de angulo
    cos_a=((a**2)-(b**2)-(c**2))/(-2*(b*c))
    rad_a= math.acos(cos_a)
    pi = math.pi
    a_angle = 180 * rad_a / pi


    cos_b=((b**2)-(a**2)-(c**2))/(-2*(a*c))
    rad_b= math.acos(cos_b)
    b_angle = 180 * rad_b / pi

    c_angle=180-a_angle-b_angle
    '''  
    if (c_angle >90):
          relleno=90+a_angle+b_angle
          c_ultimo=abs(relleno-c_angle)
          print("Angulo superior: ",c_ultimo)
    else:
          print("Angulo superior: ",c_angle)
    '''
    c_ultimo=180-c_angle
    print("Angulo superior: ",c_ultimo)
    #calculo de c
    x1_1=inflex_x[1]
    y1_1=inflex_y[1]
    x2_1=inflex_x[2]
    y2_1=inflex_y[2]

    sum1_1=((x2_1-x1_1)**2)+((y2_1-y1_1)**2)
    
    c_1=sum1_1**0.5
    
    #calculo de a
    x3_1=inflex_x[1]
    y3_1=inflex_y[1]
    x4_1=point_x[0]
    y4_1=point_y[0]
    sum2_1=((x4_1-x3_1)**2)+((y4_1-y3_1)**2)

    a_1=sum2_1**0.5
    

    #calculo de b
    x5_1=inflex_x[2]
    y5_1=inflex_y[2]
    x6_1=point_x[0]
    y6_1=point_y[0]
    sum3_1=((x6_1-x5_1)**2)+((y6_1-y5_1)**2)

    b_1=sum3_1**0.5
 


    #calculo de angulo
    cos_a_1=((a_1**2)-(b_1**2)-(c_1**2))/(-2*(b_1*c_1))
    rad_a_1= math.acos(cos_a_1)
    
    a_angle_1 = 180 * rad_a_1 / pi


    cos_b_1=((b_1**2)-(a_1**2)-(c_1**2))/(-2*(a_1*c_1))
    rad_b_1= math.acos(cos_b_1)
    b_angle_1 = 180 * rad_b_1 / pi

    c_angle_1=180-a_angle_1-b_angle_1
    '''
    if (c_angle_1 >90):
          relleno_1=90+a_angle_1+b_angle_1
          c_ultimo_1=abs(relleno_1-c_angle_1)
          print("Angulo inferior: ",c_ultimo_1)
    else:
          print("Angulo inferior: ",c_angle_1)
    '''
    c_ultimo_1=180-c_angle_1
    print("Angulo superior: ",c_ultimo_1)

    if(c_ultimo<20 or c_ultimo_1 < 20):
          print("Ligero: Se recomienda un tratamiento con ejercicios fisiologicos")
    elif (20<c_ultimo<40 or 20<c_ultimo_1 <40):
          print("Moderado: Se recomienda un tratamiento con refuerzos")
    else:
          print("Severo: Se recomienda cirugia")

    the_plot = plt.plot(x_new2, y_new)
    
    plt.plot(a_2, b_2, 'or',color='blue')
    plt.plot(point_x, point_y, 'o',color='red') #point
    #dibuja los puntos
    plt.plot(aaa,bbb,'o',color='white')
    #dibuja la linea entre ambas
    plt.plot(aaa, bbb, marker = 'o',color='red')
    titulo= nombre_archivo(file_name)
    titulo_final=titulo+'pre.png'
    path = 'static/'
    plt.savefig(os.path.join(path, titulo_final))
    return titulo_final


def img_finale(x_new2,y_new,file_name,fig,ax,a_2,b_2):
    ruta = 'flaskblog/static/'+file_name
    imagen2 = cv2.imread(ruta, cv2.IMREAD_COLOR)
    img2 = rotate(imagen2, -90)

    dimensions = imagen2.shape
    height = imagen2.shape[0]
    width = imagen2.shape[1]
    ancho = int(width)
    altura = int(height)
    width = altura

    height = ancho
    dim = (width, height)
    resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

    aa = ax.imshow(resized)

    altura = imagen2.shape[0]
    width = imagen2.shape[1]
    #y_grafo = y

    #y_inv = y[::-1]

    plt.plot(a_2, b_2, 'or')
    
    the_plot = plt.plot(x_new2, y_new)

    titulo= nombre_archivo(file_name)
    titulo_final=titulo+'doc_version.png'
    path = 'static/'
    plt.savefig(os.path.join(path, titulo_final))
    return titulo_final

def plot_rotate0(imagen,ax,width,height):
    ruta = 'static/'+imagen
    imagen2 = cv2.imread(ruta, cv2.IMREAD_COLOR)
    img2 = rotate(imagen2, -270)

    dim = (width, height)
    resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
  

    titulo = nombre_archivo(imagen)
    titulo_final = titulo+'_previous.png'
    path = 'flaskblog/static/'
    
    status = cv2.imwrite(os.path.join(path, titulo_final), resized)

    return

def plot_rotate(imagen,ax,width,height):
    ruta = 'static/'+imagen
    imagen2 = cv2.imread(ruta, cv2.IMREAD_COLOR)
    img2 = rotate(imagen2, -270)

    dim = (width, height)
    resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
  

    titulo = nombre_archivo(imagen)
    titulo_final = titulo+'_gts.png'
    path = 'flaskblog/static/'
    
    status = cv2.imwrite(os.path.join(path, titulo_final), resized)

    return
