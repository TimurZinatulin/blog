# complete
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Post, Category, Comment
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic import RedirectView
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'dadova/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'dadova/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'dadova/login_done.html', {'user': user})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'dadova/login.html', {'form': form})


def home(request):

	posts = Post.objects.order_by('-pub_date')

	paginator = Paginator(posts, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	categories = Category.objects.all()

	return render(request, 'base.html', {'page_obj': page_obj, 'posts': posts, 'categories': categories})


def about(request):

	return render(request, 'dadova/about.html')


def contact_us(request):

	return render(request, 'dadova/contact.html')

	
def show_category_posts(request, slug):
	
	category = Category.objects.get(slug=slug)

	c = Category.objects.get(slug=slug).post_set.order_by('-pub_date')
		
	paginator = Paginator(c, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
		
	return render(request, 'dadova/category.html', {'page_obj': page_obj, 'cat_posts': c, 'category': category})


class PostDetail(DetailView):

	model = Post
	template_name = 'dadova/detail.html'

	def get(self, request, post_id, *args, **kwargs):

		post = Post.objects.get(id=post_id)
		categories = Category.objects.all()
		comments = post.comment_set.order_by('-id')[:10]
		context = {
			'post': post,
			'categories': categories,
			'comments': comments,
		}

		return render(request, self.template_name, context=context)


def leave_comment(request, post_id, user_id):

	try:
		p = Post.objects.get(id=post_id)
		u = User.objects.get(id=user_id)
	except:
		raise Http404()

	p.comment_set.create(author_name=u, text=request.POST['text'])
	return HttpResponseRedirect(reverse('dadova:post_detail', args=(p.id, u.id, )))