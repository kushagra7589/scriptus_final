from django.shortcuts import render, redirect
from .forms import BlogForm, PostForm, UserForm , CommentForm
from django.contrib.auth.models import User
from .models import Post, Blog, Comment
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import datetime
from django.http import Http404, HttpResponseRedirect
# from .forms import AuthorForm

# # Create your views here.

def index(request):
	top_trending_posts_list = top_trending_posts()
	# print top_trending_posts_list
	return render (request, "home_final.html", {"list": top_trending_posts_list})

def login_user(request):
	error = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect("dashboard")
			else:
				error = "Your account is not active. Talk to the owners of the site!"
		else: 
				error =  "Invalid Credentials!"
	context = {
	"error": error
	}
	return render(request, "login.html", context)

@login_required
def dashboard(request):
	top_trending_posts_list = top_trending_posts()
	current_user = User.objects.get(username__iexact=request.user)
	blog_list_query = current_user.blog_set.all()
	# time_list = []
	blog_list = []
	for i in blog_list_query:
		blog = Blog.objects.get(blog_name__exact=i)
		blog_list.append([blog.blog_name, blog.description, blog.no_of_posts, blog.blog_created, blog.id])
	# 	time_list.append(blog.blog_created)
	# time_list.sort()

	return render(request, "dashboard.html", {"list": top_trending_posts_list, "list1": blog_list})

def register_user(request):
	form = UserForm(request.POST or None)
	errors = []
	name = []
	if request.method == "POST":
		
		name = request.POST['name'].split(" ")
		first_name = name[0]

		#first_name, last_name = first_name, last_name
		username, email, password = request.POST['username'], request.POST['email'], request.POST['password1']
		existing = User.objects.filter(username__iexact=username)
		if existing.exists():
			errors.append("This username already exists!")
			if request.POST['password1'] != request.POST['password2']:
				errors.append("The two passwords do not match!")
		else:
			if request.POST['password1'] != request.POST['password2']:
				errors.append("The two passwords do not match!") 
			else:
				new_user = User.objects.create_user(username, email, password)
				new_user.is_active = True
				new_user.first_name = first_name
				if len(name) == 2:
					last_name = name[1]
					new_user.last_name = last_name
				new_user.save()
				return HttpResponseRedirect("/login")
	return render(request, "signup.html", {"form": form, "errors": errors})

# @require_POST
# def registered(request):
# 	form = UserForm(request.POST)
# 	if form.is_valid():
# 		instance = form.save(commit = False)
# 		first_name, last_name = request.POST['name'].split(" ")
# 		instance.first_name, instance.last_name = first_name, last_name
# 		instance.save()

# 	return redirect('register/')

@login_required
def logout_user(request):
	logout(request)
	return redirect("index")

def archive_year(request, year):
	post = Post.objects.filter(post_created__year=year)
	# print post
	pos = []
	for index, i in enumerate(post):
		req_object = Post.objects.get(title__exact=i)
		pos.append([req_object.title, req_object.id, req_object.no_of_likes, req_object.no_of_comments])
		#pos[index].append(req_object.content)
	# print pos
	return render(request, "archived.html", {"year": year, "post": pos})

def archive_day(request, year, month, day):
	year1 = int(year)
	month1 = int(month)
	day1 = int(day)
	if not month1 <= 12:
		raise Http404
	elif month1 in [1, 3, 5, 7, 8, 10, 12]:
		if not day1 <= 31:
			raise Http404
		else:
			post = Post.objects.filter(post_created__year=year).filter(post_created__month=month).filter(post_created__day = day)
			# q2 = q1.filter(post_created__month=month)
			# post = q2.filter(post_created__day=day)
			# print post
			pos = []
			for index, i in enumerate(post):
				req_object = Post.objects.get(title__exact=i)
				pos.append([req_object.title, req_object.id, req_object.no_of_likes, req_object.no_of_comments])
			return render(request, "archived.html", {"year": year, "month": month, "date":day, "post": pos})
	else:
		if not day1 <=30:
			raise Http404
		else:
			post = Post.objects.filter(post_created__year=year).filter(post_created__month=month).filter(post_created__day = day)
			pos = []
			for index, i in enumerate(post):
				req_object = Post.objects.get(title__exact=i)
				pos.append([req_object.title, req_object.id, req_object.no_of_likes, req_object.no_of_comments])
			return render(request, "archived.html", {"year": year, "month": month, "date":day, "post": pos})

def archive_month(request, year, month):
	month1 = int(month)
	if month1 > 12 or month1 <= 0:
		raise Http404
	else:
		post = Post.objects.filter(post_created__year=year).filter(post_created__month=month)
		# q2 = q1.filter(post_created__month=month)
		# post = q2.filter(post_created__day=day)
		# print post
		pos = []
		for index, i in enumerate(post):
			req_object = Post.objects.get(title__exact=i)
			pos.append([req_object.title, req_object.id, req_object.no_of_likes, req_object.no_of_comments])
		return render(request, "archived.html", {"year": year, "month": month, "post": pos})

@login_required
def create_blog(request):
	blog_id = ""
	if request.method == "POST":
		form = BlogForm(request.POST)
		# print request.user
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = User.objects.get(username__iexact=request.user)
			instance.save()
			blog_id = instance.id
			# print blog_id
			return redirect("blog_page", blog = blog_id)
	else:
		form = BlogForm()
	return render(request, "create_blog.html", {})


def blog_page(request, blog):
	our_blog = Blog.objects.get(pk = blog)
	# if request.user != our_blog.author:
	# 	return render(request, "no_view.html", {})
	# else:
	lis = list(our_blog.post_set.all())
	# print lis
	post_list = []
	for i in lis:
		post = Post.objects.get(title__exact=i)
		post_list.append([post.title, post.id, post.no_of_likes, post.no_of_comments])

	context = {
		"title": our_blog.blog_name, 
		"description": our_blog.description, 
		"author": our_blog.author,
		"number": our_blog.no_of_posts,
		"blog": blog,
		"list": post_list
	}
	return render(request, "blog.html", context)

@login_required
def post_create(request, blog):
	our_blog = Blog.objects.get(pk = blog)
	form = PostForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.blog = our_blog
			instance.saved = True
			instance.save()
			our_blog.no_of_posts = our_blog.post_set.all().count()
			our_blog.save() 
			return redirect("blog_page", blog=our_blog.id)
	return render(request, "post.html", {"form": form})


def post_page(request, post_id):
	our_post = Post.objects.get(pk=post_id)
	error = None
	user_has_liked = request.user in User.objects.filter(post=our_post)
	if request.user.is_authenticated():
		current_user = User.objects.get(username__iexact=request.user)
		error = None
		if request.method == "POST":
			# print request.POST
			if "unlike" in request.POST:
				our_post.liked_user.remove(current_user)
			elif "like" in request.POST:
				our_post.liked_user.add(current_user)
				# user_has_liked = request.user in User.objects.filter(post=our_post)
			elif "comment" in request.POST:
				form = CommentForm(request.POST)
				if form.is_valid():
					instance = form.save(commit=False)
					instance.post = our_post
					instance.comment_author = current_user
					our_post.no_of_comments = Comment.objects.filter(post=our_post).count()
					instance.save()
				else:
					error = "You cannot post the same comment!"
			user_has_liked = request.user in User.objects.filter(post=our_post)
				# user_has_liked = current_user in User.objects.filter(post=our_post)
	our_post.no_of_likes = our_post.liked_user.all().count()
	our_post.no_of_comments = Comment.objects.filter(post=our_post).count()
	our_post.save()
	comments_query =  Comment.objects.filter(post=our_post)
	comments_list = []
	# print comments_query
	for i in comments_query:
		j = i.id
		comment = Comment.objects.get(pk = j)
		comments_list.append([comment.comment_content, comment.comment_author, comment.comment_created])
	context = {
			"title": our_post.title,
			"content": our_post.content,
			"no_of_likes": our_post.no_of_likes,
			"no_of_comments": our_post.no_of_comments,
			"user_has_liked": user_has_liked,
			"post_created": our_post.post_created,
			"post_updated": our_post.post_updated,
			"comments": comments_list,
			"error": error,
			"id": our_post.id
		}
	return render(request, "post_page.html", context)

def top_trending_posts():
	all_posts = Post.objects.all()
	no_of_likes_list = []
	for i in all_posts:
		post = Post.objects.get(title__exact=i)
		no_of_likes_list.append(post.no_of_likes)
	no_of_likes_list.sort()
	i = 1
	while i < len(no_of_likes_list):
		if no_of_likes_list[i] == no_of_likes_list[i-1]:
			del no_of_likes_list[i]
		i+=1
	# print no_of_likes_list
	posts_list = []
	for i in Post.objects.filter(no_of_likes=no_of_likes_list[-1]):
		post = Post.objects.get(title__exact=i)
		blog = Blog.objects.get(post=post)
		posts_list.append([post.title, blog.author, post.post_created, post.id])
		if len(posts_list) == 3:
			return posts_list
	for i in Post.objects.filter(no_of_likes=no_of_likes_list[-2]):
		post = Post.objects.get(title__exact=i)
		blog = Blog.objects.get(post=post)
		posts_list.append([post.title, blog.author, post.post_created, post.id])
		if len(posts_list) == 3:
			return posts_list
	for i in Post.objects.filter(no_of_likes=no_of_likes_list[-3]):
		post = Post.objects.get(title__exact=i)
		blog = Blog.objects.get(post=post)
		posts_list.append([post.title, blog.author, post.post_created, post.id])
		if len(posts_list) == 3:
			return posts_list


def archive(request):
	if request.method == "POST":
		if "yearsubmit" in request.POST:
			year = request.POST['year']
			return redirect("archive_year", year=year)
		elif "monthsubmit" in request.POST:
			year = request.POST['year']
			month = request.POST['month']
			return redirect("archive_month", year=year, month=month)
		elif "daysubmit" in request.POST:
			year = request.POST['year']
			month = request.POST['month']
			day = request.POST['day']
			return redirect("archive_day", year=year, month=month, day=day)
	return render(request, "archive.html", {})
