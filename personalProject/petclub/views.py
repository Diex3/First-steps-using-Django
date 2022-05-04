from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello World desde el get!", status=200) # respuesta del servicio

    def post(self, request): 

        return Response(data="Hello World desde el post!", status=200) 
    
    def patch(self, request): 

        return Response(data="Hello World desde el patch !", status=200) 

    def delete(self, request): 

        return Response(data="Hello World desde el delete !", status=200) 
    
class PetView(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello World desde el get!", status=200) # respuesta del servicio

    def post(self, request): 

        return Response(data="Hello World desde el post!", status=200) 
    
    def patch(self, request): 

        return Response(data="Hello World desde el patch !", status=200) 

    def delete(self, request): 

        return Response(data="Hello World desde el delete !", status=200) 

class PersonView(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello World desde el get!", status=200) # respuesta del servicio

    def post(self, request): 

        return Response(data="Hello World desde el post!", status=200) 
    
    def patch(self, request): 

        return Response(data="Hello World desde el patch !", status=200) 

    def delete(self, request): 

        return Response(data="Hello World desde el delete !", status=200) 

