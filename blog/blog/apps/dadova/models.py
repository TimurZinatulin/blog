# complete
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

	name = models.CharField('Имя категории', max_length=255)
	slug = models.SlugField(unique=True)

	def __str__(self):

		return self.name

	class Meta:
		verbose_name_plural = 'Categories'


class Post(models.Model):

	category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

	title = models.CharField('Название поста', max_length=255)
	subtitle = models.CharField('Подназвание поста', max_length=255)
	text = models.TextField('Текст поста')
	pub_date = models.DateField('Дата публикации')
	is_featured = models.BooleanField(default=False, null=True)
	img = models.ImageField('Изображение', null=True)

	def __str__(self):

		return self.title


class Comment(models.Model):

	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	author_name = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField('Текст комментария')