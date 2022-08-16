from django.core.exceptions import ValidationError
from django.test import TestCase
from animals.models import Animal 
from traits.models import Trait
from groups.models import Group

class AnimalTestCase(TestCase):
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

    def test_animal(self):
         print("Test for animal fields")

         self.assertEqual(self.animal_1_data["name"], self.animal_1.name)
         self.assertEqual(self.animal_1_data["age"], self.animal_1.age)
         self.assertEqual(self.animal_1_data["weight"], self.animal_1.weight)
         self.assertEqual(self.animal_1_data["sex"], self.animal_1.sex)  

    def test_animal_parameters(self):
        print("Test for animal parameters")

        animal_test_1 = Animal.objects.get(id = 1)
        name_max_length = animal_test_1._meta.get_field('name').max_length
        sex_max_length = animal_test_1._meta.get_field('sex').max_length 
        weight_max_digits = animal_test_1._meta.get_field('weight').max_digits

        self.assertEqual(name_max_length, 50) 
        self.assertEqual(sex_max_length, 15) 
        self.assertEqual(weight_max_digits, 6)   

    def test_animal_sex_invalid_choice(self):
        print("Test for animal sex invalid choice")

        self.assertRaises(ValidationError, self.animal_2.full_clean)
    
    def test_animal_may_contain_several_traits(self):
        print("Test for animal may contain several traits")
        self.animal_1.traits.set([self.trait_1, self.trait_2])

        self.assertEquals(self.animal_1.traits.count(), 2)
        self.assertIn(self.trait_1 and self.trait_2, self.animal_1.traits.all())    