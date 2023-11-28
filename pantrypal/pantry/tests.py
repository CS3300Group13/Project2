from django.test import TestCase
from users.models import Pal
from .models import PantryItem
from django.contrib.auth.models import User

class RecipeTestCase(TestCase):
    def setUp(self):
        use = User.objects.create(username="test", password="test")
        use2 = User.objects.create(username="test2", is_superuser=True)
        pal1 = Pal.objects.create(user=use, about="test")
        pal2 = Pal.objects.create(user=use2, about="test2")
        pal1.following.add(pal1)
        pal2.following.add(pal2)
        PantryItem.objects.create(pal=pal1, name="pasta", foodGroup="Grain")
        PantryItem.objects.create(pal=pal2, name="salad", foodGroup="Vegetable")

    def test_get(self):
        pal1 = Pal.objects.get(about="test")
        rec1 = PantryItem.objects.get(pal=pal1)
        rec2 = PantryItem.objects.get(name="pasta")
        rec3 = PantryItem.objects.get(foodGroup="Grain")
        self.assertEqual(rec1.pal, pal1)
        self.assertEqual(rec2.name, "pasta")
        self.assertEqual(rec3.foodGroup, "Grain")
