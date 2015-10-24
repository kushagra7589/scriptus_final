from django.contrib import admin

from .models import Author
from .forms import AuthorForm

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "email", "name"]
	form = AuthorForm
	#class Meta:
	#	model = Author

admin.site.register(Author, AuthorAdmin)