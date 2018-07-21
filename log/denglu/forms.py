from django.contrib.auth.forms import UserCreationForm
from .models import Myuser

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Myuser
        fields = ("username","email")

