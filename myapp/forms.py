from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={'class' : 'form-control border-0','placeholder':'Whats happening?'}))

    class Meta():
        model = Post
        
        fields = ('content',)