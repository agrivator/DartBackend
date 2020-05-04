from allauth.account.forms import SignupForm
from django import forms

USER_CHOICES = [
    ("customer","customer"),
    ("shopkeeper","shopkeeper"),
    ("rider","rider")
]

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone = forms.CharField(max_length=14, label='Phone Number')
    user_type = forms.ChoiceField(choices=USER_CHOICES)


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

    def save(self):

        user = super(CustomSignupForm, self).save()
        return user
