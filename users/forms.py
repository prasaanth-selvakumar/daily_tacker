from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','emp_id')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','emp_id')
class EmpIdForm(forms.ModelForm):
    emp_id = forms.CharField(max_length = 7)
    class Meta:
        model = CustomUser
        fields =("emp_id",)
    def add_emp(self):
        emp_id = self.cleaned_data.get('emp_id')
        if (not emp_id) or (emp_id==""):
            raise ValueError(_("The Employee Id must be set"))
                # Check to see if any users already exist with this email as a username.
        try:
            match = CustomeUser.objects.get(emp_id=emp_id)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return emp_id
        # A user was found with this as a username, raise an error.
        raise forms.ValidationError( "This Employee id is already in use. Please supply a different email address.")
