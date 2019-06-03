from django import forms
from .models import UserModel, PostModel, MessageBoardPost

class SignInForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']
        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')
            if password1 != password2:
                raise forms.ValidationError('Passwords Do NOt Match')

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        labels = {'title': 'Subject', 'textField': 'limit 140 characters', 'dateCreated': 'Date' }
        exclude = ['foreignkeyToUserModel']


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageBoardPost
        labels = {'title': 'Subject', 'description': 'limit 140 characters', 'dateCreated': 'Date' }
        exclude = ['foreignkeyToUserModel']
