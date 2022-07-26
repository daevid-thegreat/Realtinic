from django.forms import ModelForm
from .models import Property


class add_property_form(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


