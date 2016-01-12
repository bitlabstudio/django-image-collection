"""Models for the image_collection app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _, ugettext as __


@python_2_unicode_compatible
class ImageCollection(models.Model):
    """
    This model wraps together a collection of images.

    :name: Human readable title for this collection
    :identifier: The unique identifier for this collection

    """

    class Meta:
        ordering = ('name', 'identifier')
        verbose_name = __('image collection'),
        verbose_name_plural = __('image collections'),

    name = models.CharField(
        max_length=512,
        verbose_name=_('name'),
    )

    identifier = models.SlugField(
        unique=True,
        max_length=512,
        verbose_name=_('identifier'),
    )

    def __str__(self):  # pragma: no cover
        return '{0} ({1}): {2}'.format(
            self._meta.verbose_name.title(), self.pk, self.identifier)

    def is_public(self):
        """Returns True, if any image exists, that is currently published."""
        return self.images.filter(
            # TODO is this too complicated?
            models.Q(
                start_date__lte=now(),
                end_date__isnull=True,
            ) | models.Q(
                start_date__isnull=True,
                end_date__gte=now(),
            ) | models.Q(
                start_date__isnull=True,
                end_date__isnull=True,
            ) | models.Q(
                start_date__lte=now(),
                end_date__gte=now(),
            )
        ).exists()


@python_2_unicode_compatible
class ImageSlide(models.Model):
    """
    One image object and its extra meta information.

    :collection: The collection this image belongs to
    :image: The image file
    :alt_text: What goes into the alt attribute
    :link: If the image should link to any specific URL, put it here. Best is
      to use the ``url`` property instead of this, since that falls back to the
      image url automatically.
    :start_date: The datetime, where the image should start to be published
    :start_end: The datetime, where the image should no longer be published

    """

    class Meta:
        ordering = ('collection', 'start_date', 'end_date', 'alt_text')
        verbose_name = __('image')
        verbose_name_plural = __('images')

    collection = models.ForeignKey(
        ImageCollection,
        verbose_name=_('image collection'),
        related_name='images',
    )

    image = models.ImageField(
        upload_to='image_slides',
        verbose_name=_('image'),
    )

    alt_text = models.CharField(
        max_length=128,
        verbose_name=_('alt text'),
        help_text=_('This will go into the ``alt`` attribute of the image\'s'
                    ' HTML markup.'),
        blank=True,
    )

    link = models.URLField(
        verbose_name=_('link'),
        help_text=_('Enter URL, that the image should link to. (not required)')
    )

    start_date = models.DateTimeField(
        verbose_name=_('publish date'),
        blank=True, null=True,
    )

    end_date = models.DateTimeField(
        verbose_name=_('unpublish date'),
        blank=True, null=True,
    )

    def __str__(self):  # pragma: no cover
        return '{0} ({1}): {2}'.format(
            self._meta.verbose_name.title(), self.pk, self.alt_text)

    @property
    def url(self):  # pragma: no cover
        """Should always return a proper url."""
        return self.link.strip() or self.image.url

    @url.setter
    def url(self, value):  # pragma: no cover
        self.link = value

    @url.deleter
    def url(self):  # pragma: no cover
        self.link = ''
