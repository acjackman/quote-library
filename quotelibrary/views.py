import logging
from random import randint

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from authors.models import Author
from quotes.models import Quote


log = logging.getLogger(__name__)


def home_page(request):
    try:
        random_index = randint(0, Quote.objects.count() - 1)
        random_quote = Quote.objects.all()[random_index]
    except ValueError:
        # randint raises ValueError on trying to select from a 0 length range
        random_quote = None
    initials = Author.last_initials()
    log.debug(initials)
    context = {
        'initials': initials,
        'random_quote': random_quote,
    }
    return render(request, 'pages/home.html', context)


@staff_member_required
def raise_exception(request):
    raise Exception("Exception to verify handling. Is message where it should be?")
