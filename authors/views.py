import logging
import string

from django.core.urlresolvers import reverse
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic
from django.utils import timezone

import django_filters
from braces import views as b_views

from quotes.models import Quote
from quotes.views import QUOTE_FIELDS
from .models import Author

log = logging.getLogger(__name__)

AUTHOR_FIELDS = ['prefix', 'first_name', 'middle_name', 'last_name', 'suffix',
                 'birth_date', 'death_date', 'birth_date_year',
                 'death_date_year', 'profession', 'bio', 'notes']


class AuthorFilter(django_filters.FilterSet):
    last_initial = django_filters.CharFilter(name='last_name', lookup_expr='startswith')

    class Meta:
        model = Author
        fields = ['last_name']


class AuthorListView(generic.ListView):
    model = Author

    def get_queryset(self):
        f = AuthorFilter(self.request.GET, queryset=Author.objects.all())
        return f.qs.order_by('last_name', 'first_name', 'middle_name')

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        initials = Author.last_initials()
        log.warning(initials)
        context['initials'] = initials
        return context


class AuthorDetailView(generic.DetailView):
    model = Author


class AuthorCreateView(b_views.LoginRequiredMixin,
                       b_views.StaffuserRequiredMixin,
                       generic.CreateView):
    model = Author
    fields = AUTHOR_FIELDS


class AuthorUpdateView(b_views.LoginRequiredMixin,
                       b_views.StaffuserRequiredMixin,
                       generic.UpdateView):
    model = Author
    fields = AUTHOR_FIELDS
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse("authors:detail", kwargs={"pk": self.object.pk})


class AuthorDeleteView(b_views.LoginRequiredMixin,
                       b_views.StaffuserRequiredMixin,
                       generic.DeleteView):
    model = Author
    success_url = reverse_lazy('authors:list')


class AuthorNewQuoteView(b_views.LoginRequiredMixin,
                         b_views.StaffuserRequiredMixin,
                         generic.CreateView):
    model = Quote
    fields = [x for x in QUOTE_FIELDS if x not in ['author', 'added']]

    def form_valid(self, form):
        form.instance.author = self.get_author()
        form.instance.added = timezone.now()
        return super(AuthorNewQuoteView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AuthorNewQuoteView, self).get_context_data(**kwargs)
        context['author'] = self.get_author()
        return context

    def get_author(self):
        return Author.objects.get(pk=self.kwargs['pk'])
