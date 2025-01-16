from django import forms
from user_app.models import User

class UserForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error('password', 'Passwords do not match')
            raise forms.ValidationError("Passwords do not match")

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if User.objects.filter(first_name=first_name, last_name=last_name).exists():
            self.add_error('last_name','User with this full name already exists')
            raise forms.ValidationError("User with this full name already exists")

        return cleaned_data


class UserCreateForm(UserForm):
    repeat_password = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']


class UserUpdateForm(UserForm):
    repeat_password = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password']


class PhoneNumberField(forms.CharField):
    def clean(self, value):
        if value:
            if not all(c in "+0123456789" for c in value):
                raise forms.ValidationError(
                    "Only '+' and numbers are allowed in phone numbers."
                    )
        return super().clean(value)


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class UserInformationForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        max_length=15)

    class Meta:
        model = User
        fields = ['title', 'github_link', 'linkedin_link',
                  'phone_number', 'country', 'city',
                  'about_me', 'image']
