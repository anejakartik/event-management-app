from django import template
from django.utils.safestring import mark_safe
from event.models import Event
register = template.Library()


@register.simple_tag
def events_div():
    """
    section banner
    :return:
    """
    events = Event.objects.filter(is_active=True).order_by('title')
    print(events)
    events_div = ""
    event_div_list = ""
    for i, j in enumerate(events):
        if not i % 2:
            events_div += """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.image, j.slug, j.title)
        else:
            events_div_ = """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.image, j.slug, j.title)
            event_div_list += """<div class="col-sm-10 col-md-8 col-lg-4 m-l-r-auto">""" + events_div + events_div_ + """</div>"""
            events_div = ""

    return mark_safe(event_div_list)