from users.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2", "email", "preferences")

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit)
        preferences = self.cleaned_data.get("preferences")
        user.preferences.add(*preferences)
        return user
