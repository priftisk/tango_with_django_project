from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(cat=None):
	return {'categories': Category.objects.all()}