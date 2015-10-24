from django.shortcuts import render
from .forms import AuthorForm

# Create your views here.
def home(request):
	error =  None
	form = AuthorForm(request.POST or None)

	context = {
		"error": error,
		"form": form,
	}

	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit=False)
			user = form.cleaned_data.get('username')
			if user == "kush":
				error = "You cannot keep the username as kush!"
			else:
				instance.save()
			context = {
				"error": error,
				"form": None
				}

	return render(request, 'home.html',  context)
