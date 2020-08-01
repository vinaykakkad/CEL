from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'fields', 'autocomplete': 'off',
               'placeholder': 'Username'}
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'fields', 'autocomplete': 'off', 'placeholder': 'Email'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'fields', 'autocomplete': 'off', 'id': 'password',
               'placeholder': 'Password'}
    ))

    class meta:
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'fields', 'autocomplete': 'off',
               'placeholder': 'Username'}
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'fields', 'autocomplete': 'off', 'id': 'password',
               'placeholder': 'Password'}
    ))

    class meta:
        fields = ['username', 'email']