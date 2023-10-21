from django import template
import gostinitsa.views as views

register = template.Library()


@register.simple_tag()
def get_gostinitsas():
    return views.gostinitsa_db
