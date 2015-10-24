from django import forms

from .models import Author

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ["username", "name", "email"]
		#exclude = ['n_blogs']

	#ef clean_username():
