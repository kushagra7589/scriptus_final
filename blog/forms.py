from django import forms

from .models import Blog, Post, Comment
from django.contrib.auth.models import User


# class AuthorForm(forms.ModelForm):
# 	class Meta:
# 		model = Author
# 		fields = ["username", "name", "email"]
		#exclude = ['n_blogs']

	#ef clean_username():


class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ["blog_name", "description"]


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content"]

class UserForm(forms.Form):
	required_css_class = 'required'	
	username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label="Username",
                                error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
	email = forms.EmailField(label="E-Mail")
	password1 = forms.CharField(widget=forms.PasswordInput,
								label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput,
								label="Confirm Password")

	def clean_username(self):
		user = self.cleaned_data.get('username')
		existing = User.objects.filter(username__iexact=user)
		if existing.exists():
			raise forms.ValidationError("This username already exists!")
		else:
			return user

	def clean_email(self):
		email = self.cleaned_data.get("email")
		# usern, domain = email.split("@")
		# domain_name = [] 
		# domain_name = domain.split(".")
		# if len(domain_name) != 3:
		# 	raise forms.ValidationError("Please provide a iiitd email-ID")
		# elif domain_name[0] != 'iiitd' or domain_name[1] != "ac" or domain_name[2] != "in":
		# 	raise forms.ValidationError("Please provide a iiitd email-ID")
		# else:
		return email

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("The two passwords do not match!")
		return self.cleaned_data

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_content']

class BlogFormAdmin(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['blog_name', 'description', 'author']

