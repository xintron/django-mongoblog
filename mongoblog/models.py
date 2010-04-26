from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from mongoengine import *
import datetime


class Entry(Document):
    STATUS_PUBLIC = 1
    STATUS_DRAFT = 2

    STATUS_DEFAULT = STATUS_DRAFT

    status_choices = (
        (STATUS_PUBLIC, _('public')),
        (STATUS_DRAFT, _('draft')),
    )

    TYPE_POST = 1
    TYPE_QUOTE = 2
    TYPE_IMAGE = 3

    TYPE_DEFAULT = TYPE_POST

    type_choices = (
        (TYPE_POST, _('post')),
        (TYPE_IMAGE, _('image')),
        (TYPE_QUOTE, _('quote')),
    )

    title = StringField(max_length=100, required=True)
    body = StringField(required=True)

    slug = StringField(unique=True, max_length=100)
    status = IntField(required=True)
    type = IntField(required=True)

    created = DateTimeField(default=datetime.datetime.now)

    meta = {
        'ordering': ['-created'],
        'indexes': ['slug']
    }

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.status:
            self.status = self.STATUS_DEFAULT
        if not self.type:
            self.type = self.TYPE_DEFAULT

        super(Entry, self).save()

    def get_absolute_url(self):
        return reverse('blog_entry_detail', args = [self.slug])
