"""Templatetags for the image_collection app."""
from django import template

from ..models import ImageCollection


register = template.Library()


@register.inclusion_tag(takes_context=True,
                        file_name='image_collection/tags/bs3_carousel.html')
def render_bs3_carousel(context, identifier):
    """Renders an image collection as Bootstrap 3 carousel."""
    try:
        collection = ImageCollection.objects.get(identifier=identifier)
    except ImageCollection.DoesNotExist:
        collection = None
    context.update({'collection': collection})
    return context
