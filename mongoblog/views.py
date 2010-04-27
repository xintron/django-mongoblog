from django.http import Http404
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template

from models import Entry

def entry_list(request, **kwargs):
    entries = Entry.objects(status = Entry.STATUS_PUBLIC)
    # TODO: Paginate the Entry-list

    return direct_to_template(request, 'mongoblog/entry_list.html', {
        'entry_list': entries,
    })

def entry_detail(request, slug):
    entry = Entry.objects(slug=slug).first()
    if not entry:
        raise Http404

    return direct_to_template(request, 'mongoblog/entry_detail.html', {
        'entry': entry,
    })
