from rest_framework.views import APIView,Request,Response, status
from .models import Group
from django.forms.models import model_to_dict
from .serializers import GroupSerializer

# Create your views here.

class GroupView(APIView):
    def get(self,request: Request):
        groups = Group.objects.all()
        groups_list = [model_to_dict(animal) for animal in groups]
        return Response(groups_list)


    def post(self,request:Request):
        serializer = GroupSerializer(data=request.data)

        print(serializer,"seria")

        if not serializer.is_valid():
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

        Group.objects.create(**serializer.validated_data)
      
        return Response(serializer.validated_data, status.HTTP_201_CREATED)