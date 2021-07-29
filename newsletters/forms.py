from django import forms

from .models import NewsletterUser

class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.clean_data.get('email')

            return email
