import logging
import string

from django.core.urlresolvers import reverse
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

import django_filters
from braces import views as b_views

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
        return f.qs

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)

        initials = set(string.ascii_uppercase)
        author_names = Author.objects.values('last_name').distinct()
        for obj in author_names:
            initials.add(obj['last_name'][0])
        acj = list(initials)
        acj.sort()
        context['initials'] = acj
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
