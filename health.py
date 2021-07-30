import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def start():
	print('Monitoreo de la salud')
	print('Ingresar la fecha y los datos correspondientes')
	print('elegir una opcion:')
	print('1: ingresar datos')
	print('2: recolectar datos y realizar estadistica')
	print('3: salir')
	option=input('ingresa la opcion: ')
	if option == '1':
		fecha=input('ingresa la fecha en formato dd/mm/aaaa: ')
		hora=input('ingresa la hora en formato hh:mm:ss: ')
		fecha2=get_numb(fecha)
		dd=int(fecha2[0])
		mm=int(fecha2[1])
		aa=int(fecha2[2])
		nombre=input('ingresa nombre de la persona: ')
		tenalta=input('ingresa presión sistólica (alta): ')
		tenbaja=input('ingresa presión diastólica (baja): ')
		pulso=input('ingresa pulsaciones por minuto: ')
		peso=input('ingresa peso (kg): ')
		altafloat=float(tenalta)
		bajafloat=float(tenbaja)
		pulsofloat=float(pulso)
		pesofloat=float(peso)
		obs=input('ingresa observacion: ')
		print (nombre+'. '+'dia:'+str(dd) +', mes:'+str(mm)+', año:'+str(aa)+', presión sistólica:'+ str(tenalta) +', presión diastólica: '+str(tenbaja)+ ', pulsaciones por minuto: '+str(pulso)+ ', peso: '+str(peso)+ ', observaciones:'+ obs)
		data={'Nombre':nombre, 'Fecha':fecha, 'Hora':hora, 'Presion sistolica':altafloat, 'Presion diastolica':bajafloat, 'Pulsaciones':pulsofloat, 'Peso':pesofloat, 'Observaciones':obs}
		df = pd.DataFrame(data,index=[0]) 
		#d = [nombre,fecha,hora,altafloat,bajafloat,pulsofloat,pesofloat,obs]
		#df=pd.DataFrame(d, columns = ['Nombre', 'Fecha','Hora','tension alta','tension baja','pulsaciones','peso','observaciones']) 
		
		directory = 'datos/'

		if not os.path.exists(directory):
			os.makedirs(directory)
		writepath=directory+'datos.csv'    
		mode = 'a' if os.path.exists(writepath) else 'w'
		if mode=='w':
			df.to_csv(writepath, index = False, header = True,mode='w')
		else:
			df.to_csv(writepath, index = False, header = False,mode='a')
		#with open(writepath,mode) as f:
    		#	f.write('\n')    
		
		print('----------------------')
		return 1
	elif option=='2': #hacer estadistica y leer archivos
		print ("seleciona una opcion")
		print("1: estadistica temporal")#+"\n"+"2:estadistica acumulada")
		print("2: volver")
		option2=input("ingresa opcion: ")
		if option2=='1':
			
			datos = pd.read_csv('datos/datos.csv')
			print('Hay datos de: '+str((datos.Nombre.unique())))
			#datos[['Fecha', 'Hora']] = datos[['Fecha', 'Hora']].apply(pd.to_datetime)
			datos['time']=pd.to_datetime(datos['Fecha']  +' '+ datos['Hora'],format='%d/%m/%Y %H:%M:%S')
			datos.sort_values(by='time',inplace=True)
			#datos.index=datos.Hora
			#pd.to_datetime(datos[['Fecha','Hora']],format='%dd/%mm/%Y%H:%M:%S')
			#pd.to_datetime(datos,infer_datetime_format=True)
			#datos.to_csv('test2.csv')
			option3=input('escriba el nombre de la persona para realizar el grafico: ')
			datos2=datos[datos.Nombre==option3]
			#datos2['Observaciones']=datos2['Observaciones'].fillna[' ']
			#datos2['Observaciones']= datos2['Observaciones'].replace(r'', ' ', regex=True)
			#print(datos2)
			#pd.plotting.autocorrelation_plot(datos["Peso"].resample("1y").median())
			#print(datos)
			
			fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,sharex=True,figsize=(10,10))
			fig.suptitle(option3)
			# Add x-axis and y-axis
			ax1.plot(datos2['time'],
        			datos2['Presion sistolica'],
        			color=[0.4,0.45,0.0],marker='o', linestyle='--')
			#ax1.set_xticklabels(ax1.get_xticklabels(),rotation=45)
			# Set title and labels for axes
			#ax1.set(xlabel="Tiempo",
			ax1.set(ylabel="Presión sistólica")
			ax2.plot(datos2['time'],
        			datos2['Presion diastolica'],
        			color=[0.4,0.45,0.0],marker='o', linestyle='--')
			#ax2.set_xticklabels(ax.get_xticklabels(),rotation=45)
			# Set title and labels for axes
			#ax2.set(xlabel="Tiempo",
			ax2.set(ylabel="Presión diastólica")    			   
			ax3.plot(datos2['time'],
        			datos2['Pulsaciones'],
        			color=[0.4,0.45,0.0],marker='o', linestyle='--')
			#ax3.annotate(datos2['Observaciones'],(datos2['time'],datos2['Pulsaciones']),rotation=90)
			for index, row in datos2.iterrows():
				if isnan(row['Observaciones'])==False:
					ax3.annotate(row['Observaciones'], (row['time'], row['Pulsaciones']),rotation=90,
						xytext=(row['time'], row['Pulsaciones']+(datos2['Pulsaciones'].max()-datos2['Pulsaciones'].min())/5),
						bbox=dict(boxstyle="round", alpha=0.1,color=[0.4,0.45,0.0]),arrowprops = 
						dict(facecolor=[0.4,0.45,0.0],arrowstyle="fancy"))
			#ax3.get_xticklabels.set_rotation(45)
			ax3.tick_params(labelrotation=45)
			# Set title and labels for axes
			ax3.set(xlabel="Tiempo",
    			   ylabel="Pulsaciones")    			   			
			ax4.plot(datos2['time'],
        			datos2['Peso'],
        			color=[0.4,0.45,0.0],marker='o', linestyle='--')
			#ax4.annotate(datos2['Observaciones'],(datos2['time'],datos2['Peso']),rotation=90)
			for index, row in datos2.iterrows():
				if isnan(row['Observaciones'])==False:
					ax4.annotate(row['Observaciones'], (row['time'], row['Peso']),rotation=90,
						xytext=(row['time'], row['Peso']+(datos2['Peso'].max()-datos2['Peso'].min())/5),
						bbox=dict(boxstyle="round", alpha=0.1,color=[0.4,0.45,0.0]),arrowprops = 
						dict(facecolor=[0.4,0.45,0.0],arrowstyle="fancy"))
			#ax4.set_xticklabels(ax4.get_xticklabels(),rotation=45)
			ax4.tick_params(labelrotation=45)
			# Set title and labels for axes
			ax4.set(xlabel="Tiempo",
    			   ylabel="Peso (Kg)")
			#fig.xticks(rotation=90)
			fig.show()
			#fig.savefig('salud de '+option3+'.pdf',bbox_inches='tight')
			fig.savefig('salud de '+option3+'.pdf')
			
			#datos2.to_csv('test.csv')
			
			
			
		print('----------------------')

		return 1
	elif option=='3':
		print('Goodbye')
		return 3
		
	else:
		print('Por favor, elige una opcion correcta')
		print('----------------------')
		return 1

def get_numb(x):
	return x.split('/')
	
def get_entries(x):
	return x.split(',')
def get_variables(x):
	return x.split(':')

def isnan(value):
  try:
      import math
      return math.isnan(float(value))
  except:
      return False

while True:
	if start()==3:
		break
		
		

