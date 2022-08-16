from rest_framework.views import APIView,Request,Response, status
from .models import Trait
from django.forms.models import model_to_dict
from .serializers import TraitSerializer


class TraitView(APIView):
    def get(self,request: Request):
        traits = Trait.objects.all()
        traits_list = [model_to_dict(trait) for trait in traits]
        return Response(traits_list)


    def post(self,request:Request):
        
        serializer = TraitSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

        Trait.objects.create(**serializer.validated_data)
      
        return Response(serializer.validated_data, status.HTTP_201_CREATED)