from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = "form-control bg-dark text-white mb-4"
        self.fields['username'].widget.attrs["placeholder"] = "Enter Username"
        self.fields['username'].widget.attrs["required"] = "true"

        self.fields['email'].widget.attrs["class"] = "form-control bg-dark text-white mb-4"
        self.fields['email'].widget.attrs["placeholder"] = "Enter Email"
        self.fields['email'].widget.attrs["required"] = "true"

        self.fields['password1'].widget.attrs["class"] = "form-control bg-dark text-white mb-4"
        self.fields['password1'].widget.attrs["placeholder"] = "Enter Password"
        self.fields['password1'].widget.attrs["required"] = "true"

        self.fields['password2'].widget.attrs["class"] = "form-control bg-dark text-white mb-4"
        self.fields['password2'].widget.attrs["placeholder"] = "Re-Enter Password"
        self.fields['password2'].widget.attrs["required"] = "true"