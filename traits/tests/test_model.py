from django.test import TestCase
from traits.models import Trait
from animals.models import Animal
from groups.models import Group
from django.db.utils import IntegrityError

class TraitTestCase(TestCase):
    @classmethod

    def setUpTestData(cls) -> None:

        cls.animal_1_data = {
            
            "name": "athena",
            "age": 1,
            "weight": 30,
            "sex": "Femea",
        }

        cls.animal_2_data = {
             "name": "kratos",
            "age": 1,
            "weight": 30,
            "sex": "Indefinido",
        }

        cls.group_1_data = {
            "name": "cão", 
            "scientific_name": "canis familiaris"
        }

        cls.traits_1_data = {
            "name": "careca"
        }

        cls.traits_2_data = {
            "name": "médio porte"
        }

        cls.traits_1 = Trait.objects.create(**cls.traits_1_data)
        cls.traits_2 = Trait.objects.create(**cls.traits_2_data)
        cls.group_1 = Group.objects.create(**cls.group_1_data)
        cls.animal_1 = Animal.objects.create(**cls.animal_1_data)
        cls.animal_2 = Group.objects.create(**cls.animal_2_data)

    def test_trait(self):
         print("Test for trait fields")

         self.assertEqual(self.traits_1_data["name"], self.traits_1.name)

    def test_animal_parameters(self):
        print("Test for animal parameters")

        
        name_max_length = self.traits_1._meta.get_field('name').max_length   
        self.assertEqual(name_max_length, 20)

    def test_unique_trait(self):
        print("Test for unique trait property")
        with self.assertRaises(IntegrityError):
            Trait.objects.create(**self.traits_1_data)    

    def test_trait_several_animals(self):
        print("Test for traits may contain several animals")
        self.animal_1.traits.add(self.traits_1)
        self.animal_2.traits.add(self.traits_1)

        self.assertEquals(self.traits_1.animals.count(), 2)
        self.assertIn(self.animal_2 and self.animal_2, self.traits_1.animals.all())        