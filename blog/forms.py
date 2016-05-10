from django import forms
from .models import Post

# .models means file models ada dalam satu direktori dengan file forms
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text',)
		