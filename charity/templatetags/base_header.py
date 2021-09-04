from django import template

register = template.Library()

@register.inclusion_tag('header.html')
def category_navbar():
    pass