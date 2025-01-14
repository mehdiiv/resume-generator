from django import forms
from user_app.models import User


class UserCreateForm(forms.ModelForm):
    repeat_password = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error('password', 'Passwords do not match')
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    repeat_password = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            self.add_error('password', 'Passwords do not match')
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


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
