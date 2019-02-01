from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="Введите Ваш login",
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'style': 'margin: 0.5vw; padding:1vw;height:3vh;',
                                      'class': 'form-control col-sm-8',
                                      'placeholder': 'Введите Ваш логин'
                                      }),
    )

    password = forms.CharField(
        label="Введите Ваш пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'style': 'margin:0.5vw; padding:1vw;height:3vh;',
            'class': 'form-control col-sm-8',
            'placeholder': 'Введите Ваш пароль'
        }),
    )

    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)


class UserCreation(UserCreationForm):
    error_messages = {
        'password_mismatch': "Поля ввода пароля должны совпадать",
    }
    username = UsernameField(
        label="Введите Ваш login",
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'style': 'margin: 0.5vw; padding:1vw;height:3vh;',
                                      'class': 'form-control col-sm-8',
                                      'placeholder': 'Введите Ваш логин'
                                      }),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'style': 'margin: 0.5vw; padding:1vw;height:3vh;',
            'class': 'form-control col-sm-8',
            'placeholder': 'Введите Ваш пароль'
        }),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={
            'style': 'margin:0.5vw; padding:1vw;height:3vh;',
            'class': 'form-control col-sm-8',
            'placeholder': 'Подтвердите пароль'
        }),
        strip=False,
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
        # тут мы очищаем поля подсказок
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

    # def __init__(self, *args, **kwargs):
        # for field in self.base_fields.values():
        #     field.widget.attrs['placeholder'] = field.label
        # super(UserCreationForm, self).__init__(*args, **kwargs)