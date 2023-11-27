from django.forms import ModelForm
from .models import PantryItem


class PantryItemForm(ModelForm):
    class Meta:
        model = PantryItem
        fields = ["name", "foodGroup"]
