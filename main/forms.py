from .models import Customers
from django.forms import ModelForm, TextInput, Textarea

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = ['Name', 'Email', 'Message']

        widgets = {
            "Name": TextInput(attrs={'placeholder': 'Name'}),
            "Email": TextInput(attrs={'placeholder': 'Email', 'pattern ': "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,4}$"}),
            "Message": Textarea(attrs={'placeholder': 'Message'})
        }