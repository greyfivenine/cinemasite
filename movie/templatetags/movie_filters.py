import hashlib
import urllib.parse
from django import template
from django.utils.safestring import mark_safe
from django.http import QueryDict
from django.utils import timezone

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=100):
    default = "identicon"
    # robohash, retro, identicon
    # https://www.gravatar.com/avatar/cb69cd596f305fa5f24a998a817a160a?d=identicon
    return "https://www.gravatar.com/avatar/%s?%s" % (hashlib.md5(bytes(email.lower(),"UTF-8")).hexdigest(), urllib.parse.urlencode({'d':default, 's':str(size)}))

@register.filter
def now_schedule(sc):
    now = timezone.now()
    return sc.filter(movie_date__gte=now)

@register.filter
def now_schedule_count(sc):
    now = timezone.now()
    return sc.filter(movie_date__gte=now).count()
