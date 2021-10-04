from . import views
from django.urls import path


app_name = 'dadova'
urlpatterns = [
	path('register/', views.register, name='register'),
	path('user_login/', views.user_login, name='login'),
	path('', views.home, name='home'),
	path('<int:post_id>/<int:user_id>/', views.PostDetail.as_view(), name='post_detail'),
	path('about/', views.about, name='about'),
	path('contact_us/', views.contact_us, name='contact_us'),
	path('<str:slug>/', views.show_category_posts, name='show_category_posts'),
	path('<int:post_id>/<int:user_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]