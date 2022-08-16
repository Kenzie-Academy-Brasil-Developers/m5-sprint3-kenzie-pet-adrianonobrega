
from email.headerregistry import Group
from xml.dom import ValidationErr
from rest_framework.views import APIView,Request,Response, status
import animals

from traits.models import Trait
from .models import Animal
from django.forms.models import model_to_dict
from .serializers import AnimalSerializer
from  django.shortcuts import get_object_or_404
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from django.core.exceptions import ValidationError
# Create your views here.
import pdb

from animals import serializers

class AnimalView(APIView):
    
    def get(self,request: Request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)


    def post(self,request:Request) -> Response:
        
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data,status.HTTP_201_CREATED)


class AnimalDetailView(APIView):

    def get(self,request: Request, animal_id: int)-> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        serializers = AnimalSerializer(animal)
        return Response(serializers.data)


    def patch(self,request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        serializers = AnimalSerializer(animal,request.data, partial=True)
        serializers.is_valid(raise_exception = True)   
  
        try:
            serializers.save()

        except ValidationError as err:
            return Response(err.args[0],status.HTTP_422_UNPROCESSABLE_ENTITY)


        return Response(serializers.data,status.HTTP_200_OK)
       
        
    def delete(self,request: Request, animal_id: int) -> Response:
        animal = get_object_or_404(Animal, id=animal_id)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)