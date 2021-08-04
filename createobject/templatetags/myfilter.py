from django import template

register = template.Library()


@register.filter(name="type")  # name 是 html 中的过滤器名
def typeof(arg):
    return type(arg).__name__
