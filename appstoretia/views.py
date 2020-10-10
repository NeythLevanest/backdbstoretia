from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from appstoretia.models import *
from appstoretia.serializers import *

from django.db.models import Sum, Avg
from django.db.models import Max, Min
#Data Libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

class UsuariosViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer 

class CaracteristicasViewSet(viewsets.ModelViewSet):
    queryset = Caracteristicas.objects.all()
    serializer_class = VentasSerializer

class TiendasViewSet(viewsets.ModelViewSet):
    queryset = Tiendas.objects.all()
    serializer_class = TiendasSerializer

class Correlacion_Ventas(APIView):
    def get(self, request, format=None):
        ventas_tiendas = Ventas.objects.select_related('store')[0:100].values("weekly_sales", "store__size")
        print("hola")
        data = pd.DataFrame(list(ventas_tiendas))
        print(data.shape)
        data.head()
        
        ##Capturamos columnas
        columnas = list(data.columns)
        #print(columnas)
        #print(data)
        #ventas = data['weekly_sales']
        #print(type(ventas))
        #size_store = data['store__size'] 
        #print(size_store)
        #print(type(size_store))
        #resultado = np.corrcoef(ventas.astype(float), size_store.astype(float))
        #print(resultado)

        data2 = data.iloc[:,:2]
        cordata = data2.corr()
        print(cordata)
        sns.heatmap(cordata, annot = True)

        plt.show()
        #print(data)
        #print(ventas_tiendas)
        #for e in ventas_tiendas:
        #    print(e.weekly_sales)
        #print("Hola")
        
       
        #return Response(ventas_tiendas, status=status.HTTP_201_CREATED)
class Total_Ventas(APIView):
    def get(self, request,format=None):
        ventas_tienda = ''
       
     
        ventas_tienda = Ventas.objects.values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
        caracteristicas = Tiendas.objects.values("size", "type")
        
        respuesta = {"tienda":ventas_tienda,"caracteristicas":caracteristicas}
        
        return Response(respuesta, status=status.HTTP_201_CREATED)
    def post(self, request, format=None):
        ventas_tienda = ''
        
        date_init = str(request.data["date_init"])
        date_end = str(request.data["date_end"])
        feriado = request.data["feriado"]

        fecha_min = Ventas.objects.values('date').order_by('date').first()
        print("min", fecha_min)
        fecha_max = Ventas.objects.values('date').order_by('date').last()
        print("max", fecha_max)

        if(feriado == ""):

            if(date_init == "" and date_end != ""):
                ventas_tienda = Ventas.objects.filter(date__range=[fecha_min,date_end]).values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
            
            elif(date_init != "" and date_end == ""):
                ventas_tienda = Ventas.objects.filter(date__range=[date_init,date.today()]).values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
            
            elif(date_init == "" and date_end == ""):  
                ventas_tienda = Ventas.objects.values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
            
            elif(date_init != "" and date_end != ""): 
                ventas_tienda = Ventas.objects.filter(date__range=[date_init,date_end]).values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))

        else:
            if(feriado=="true"):
                feriado = True
            else:
                feriado = False
            if(date_init == "" and date_end != ""):
                ventas_tienda = Ventas.objects.filter(date__range=[fecha_min,date_end]).filter(isholiday=feriado).values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
            
            elif(date_init != "" and date_end == ""):
                ventas_tienda = Ventas.objects.filter(date__range=[date_init,date.today()]).filter(isholiday=feriado).values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
            
            elif(date_init == "" and date_end == ""):  
                ventas_tienda = Ventas.objects.values('store').filter(isholiday=feriado).annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
            
            elif(date_init != "" and date_end != ""): 
                ventas_tienda = Ventas.objects.filter(date__range=[date_init,date_end]).filter(isholiday=feriado).values('store').annotate(sumsales = Sum('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))


        caracteristicas = Tiendas.objects.values("size", "type")
        
        respuesta = {"tienda":ventas_tienda,"caracteristicas":caracteristicas}
        
        return Response(respuesta, status=status.HTTP_201_CREATED)
class Promedio_Ventas(APIView):
    def post(self, request, format=None):
        caracteristicas = ''
        ventas_departamento = ''
        ventas_tienda = ''
        sum_unemployme =''
        
        num_tienda = request.data["store"]
        date_init = str(request.data["date_init"])
        date_end = str(request.data["date_end"])
        feriado = request.data["feriado"]
        valor = num_tienda
     
        print("fechainit", date_init)

        fecha_min = Ventas.objects.values('date').order_by('date').first()
        print("min", fecha_min)
        fecha_max = Ventas.objects.values('date').order_by('date').last()
        print("max", fecha_max)

        caracteristicas = Tiendas.objects.filter(store=valor).values("size", "type")

        if(feriado == ""):
            if(date_init == "" and date_end != "" ):
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(date__range=[fecha_min,date_end]).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(date__range=[fecha_min,date_end]).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).filter(date__range=[fecha_min,date_end]).values('store').annotate(sumunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
            
            elif(date_init != "" and date_end == ""):
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date.today()]).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date.today()]).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).filter(date__range=[date_init,date.today()]).values('store').annotate(avgunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
            
            elif(date_init == "" and date_end == ""):  
                ventas_departamento = Ventas.objects.filter(store_id=valor).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).values('store').annotate(avgunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
            
            elif(date_init != "" and date_end != ""): 
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date_end]).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date_end]).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).filter(date__range=[date_init,date_end]).values('store').annotate(avgunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
       
        else:
            if(feriado=="true"):
                feriado = True
            else:
                feriado = False
            if(date_init == "" and date_end != "" ):
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(date__range=[fecha_min,date_end]).filter(isholiday=feriado).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(date__range=[fecha_min,date_end]).filter(isholiday=feriado).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).filter(date__range=[fecha_min,date_end]).values('store').annotate(sumunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
            
            elif(date_init != "" and date_end == ""):
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date.today()]).filter(isholiday=feriado).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date.today()]).filter(isholiday=feriado).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).filter(date__range=[date_init,date.today()]).values('store').annotate(avgunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
            
            elif(date_init == "" and date_end == ""):  
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(isholiday=feriado).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(isholiday=feriado).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).values('store').annotate(avgunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))
            
            elif(date_init != "" and date_end != ""): 
                ventas_departamento = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date_end]).filter(isholiday=feriado).values('departamento').annotate(avgsales = Avg('weekly_sales'))
                ventas_tienda = Ventas.objects.filter(store_id=valor).filter(date__range=[date_init,date_end]).filter(isholiday=feriado).values('store').annotate(avgsales = Avg('weekly_sales'), max=Max('weekly_sales'), min=Min('weekly_sales'))
                sum_unemployme = Caracteristicas.objects.filter(store_id=valor).filter(date__range=[date_init,date_end]).values('store').annotate(avgunemploye = Avg('unemployme'), max=Max('unemployme'), min=Min('unemployme'))                
        
        respuesta = {"tienda":ventas_tienda,"caracteristicas":caracteristicas,"desempleo":sum_unemployme,"p_departamentos":ventas_departamento}
        
        return Response(respuesta, status=status.HTTP_201_CREATED)

class Promedio_Global_Ventas(APIView):
     def post(self, request, format=None):
        num_tienda = request.data["store"]
        valor = num_tienda
        print("Valor:", valor)
        ventas_tienda = Ventas.objects.filter(store_id=valor).values('store_id').annotate(avgsales = Avg('weekly_sales'))
        respuesta = {"tienda":ventas_tienda}
        return Response(respuesta, status=status.HTTP_201_CREATED)