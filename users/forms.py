from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['user_type'] = forms.CharField(required=True)

    def save(self, request):
        user_type = self.cleaned_data.pop('user_type')
        user = super(MyCustomSignupForm, self).save(request)
        return user