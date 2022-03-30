from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NuestraCreacionUser(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir password',
                                widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {
            k: '' for k in fields
        }

        # list_comprenhension (en este caso con diccionarios)
        # algo para que pase for valor in valores
        
class NuestraEdicionUser(forms.Form):
    
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(
                                label='Nombre',
                                max_length=20,
                                required=False
                                )
    last_name = forms.CharField(
                                label='Apellido',
                                max_length=20
                                )
    password1 = forms.CharField(
                                label='Password',
                                widget=forms.PasswordInput()
                                )
    password2 = forms.CharField(
                                label='Repetir password',
                                widget=forms.PasswordInput()
                                )