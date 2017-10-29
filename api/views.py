from rest_framework import viewsets

from authors.models import Author
from quotes.models import Quote

from .permissions import IsAdminOrReadOnly
from .serializers import AuthorSerializer, QuoteSerializer, CreateAuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = (IsAdminOrReadOnly, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAuthorSerializer
        else:
            return AuthorSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (IsAdminOrReadOnly, )
