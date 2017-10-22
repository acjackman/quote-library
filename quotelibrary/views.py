from random import randint

from django.shortcuts import render

from quotes.models import Quote


def home_page(request):
    try:
        random_index = randint(0, Quote.objects.count() - 1)
        random_quote = Quote.objects.all()[random_index]
    except ValueError:
        # randint raises ValueError on trying to select from a 0 length range
        random_quote = None
    context = {
        'random_quote': random_quote
    }
    return render(request, 'pages/home.html', context)
