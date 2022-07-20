
from ast import Div
from attr import fields
from django.forms import ModelForm
#custome forms
from django import forms
from .models import UserProfile, Subscriber
from django.contrib.auth.models import User

#crispy forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,  Row, Column, Fieldset

class UserRegistrationForm(forms.Form):
    

    username = forms.CharField(
        label= 'Username',
        max_length=100,
        required=True
    )
    email = forms.EmailField(
        label='Email',
        max_length=200,
        required=True
    )

    password_1 = forms.CharField(max_length=32,
    label='Password',
    widget=forms.PasswordInput)
    
    password_2 = forms.CharField(max_length=32,
    label='Retype Password',
    widget=forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'register'

        self.helper.add_input(Submit('submit', 'Submit',css_class="btn-success"))
        self.helper.layout = Layout(
            Fieldset(
            'Sign Up',
            'username',
            'email',
            'password_1',
            'password_2',
            css_class = 'form-outline mb-4')

        )

"""class UserRegistrationModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']"""

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label= 'Username',
        max_length=100,
        required=True
    )
    password = forms.CharField(max_length=32,
    label='Password',
     widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'login'
        self.helper.add_input(Submit('submit', 'Submit', css_class="btn-success"))
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0')
            ),
            Row(
                Column('password', css_class='form-group col-md-6 mb-0')
            )
        )

class SubscriberForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'login'
        self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model = Subscriber
        fields = ['email', 'name']

    
class EditAccountForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'login'
        self.helper.add_input(Submit('submit', 'Submit'))


        class Meta:
            model = UserProfile
            fields = '__all__'
