from django import forms


class nuestra_creacion_user(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput())

    first_name = forms.CharField(label='Nombre', max_length=20, required=False)
    last_name = forms.CharField(label='Apellido', max_length=20)

    class Meta:
        model = User
        field = []