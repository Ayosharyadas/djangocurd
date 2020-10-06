
from django import forms
from Farmer.models import Farmermodel
class FarmersForm(forms.ModelForm):
    class Meta:
        model = Farmermodel
        fields = "__all__"