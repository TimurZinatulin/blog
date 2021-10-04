from django.views.generic.detail import SingleObjectMixin


class CategoryMixin(SingleObjectMixin):

	paginate_by = 2