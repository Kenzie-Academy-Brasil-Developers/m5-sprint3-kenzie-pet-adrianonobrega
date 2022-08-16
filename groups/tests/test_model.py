from django.test import TestCase
from animals.models import Animal
from groups.models import Group
import pdb

class GroupTestCase(TestCase):
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

     

      
        cls.group_1 = Group.objects.create(**cls.group_1_data)
        cls.animal_1 = Animal.objects.create(**cls.animal_1_data)
        cls.animal_2 = Group.objects.create(**cls.animal_2_data)

    def test_group(self):
         print("Test for group")

         self.assertEqual(self.group_1_data["name"], self.group_1.name)
         self.assertEqual(self.group_1_data["scientific_name"], self.group_1.scientific_name)

    def test_group_parameters(self):
        print("Test for group parameters")

        group_test_1 = Group.objects.get(id=1)
        name_max_length = group_test_1._meta.get_field('name').max_length
        scientific_name_max_length = group_test_1._meta.get_field('scientific_name').max_length

        self.assertEqual(name_max_length, 20) 
        self.assertEqual(scientific_name_max_length, 50)

    def test_group_may_contain_animals(self):
        self.assertEquals(len(Animal.objects.filter(group_id=1)), 2)    