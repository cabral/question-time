from django_registration.forms import RegistrationForm
from QuestionTime.users.models import CustomUser

class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser