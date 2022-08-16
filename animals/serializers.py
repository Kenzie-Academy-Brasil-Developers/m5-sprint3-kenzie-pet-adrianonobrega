import pdb
from groups.models import Group
from traits.models import Trait
from .models import Animal, Sex
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from rest_framework import serializers
from django.core.exceptions import ValidationError
from math import log

class AnimalSerializer(serializers.Serializer):

    invalid_key_update = {'traits','group', 'sex'}

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField( choices=Sex.choices,default=Sex.default)

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def calculate_human_age(self,animal):
        return 16 * log(animal.age) + 31



    def create(self, validated_data):
        #Separar informações que estão vindo da sua requisição para preencheras respectivas models (Animal, Group e Trait)
        # Verificar se o group existe, caso não exista você deve criar
        # Utilização do método get_or_create, para fazer a verificação se existe ou não ou se cria ou não, na parte de Group e Characteristics https://docs.djangoproject.com/en/4.0/ref/models/querysets/ da um ctrl f e procura por get_or_create
        # Instanciar Animal com suas informações atrelando o group criado
        # O mesmo processo de para group, lembrando que traits é uma lista de trait

        valueGroup = validated_data.pop('group')
        valueTrait = validated_data.pop('traits')

        
        
        group_value,_ = Group.objects.get_or_create(**valueGroup)
        traits_value = [Trait.objects.get_or_create(**trait)[0] for trait in valueTrait]
        animal = Animal.objects.create(**validated_data,group=group_value) #criando Animal
        animal.traits.set(traits_value)

        
        

        return animal



    def update(self, instance, validated_data):


        invalid_key = self.invalid_key_update.intersection(set(validated_data))
        
        if invalid_key:
            response_error = {key: f"You can not update {key} property" for key in invalid_key}
            raise ValidationError(response_error)

        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()
      
        return instance

        
    