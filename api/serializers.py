from django.utils import timezone

from rest_framework import serializers

from authors.models import Author
from quotes.models import Quote


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'prefix',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'birth_date',
            'death_date',
            'birth_date_year',
            'death_date_year',
            'profession',
            'bio',
            'notes',
        )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'id',
            'text',
            'author',
            'added',
            'date',
            'source',
            'reference',
            'verified',
            'rating',
        )
        extra_kwargs = {
            'added': {'required': False}
        }

    def create(self, validated_data):
        if 'added' not in validated_data:
            validated_data['added'] = timezone.now()
        return super().create(validated_data)


class NestedQuoteSerializer(QuoteSerializer):
    class Meta(QuoteSerializer.Meta):
        model = Quote
        fields = tuple(x for x in QuoteSerializer.Meta.fields if x != 'author')


class CreateAuthorSerializer(AuthorSerializer):
    quotes = NestedQuoteSerializer(many=True, required=False)

    class Meta(AuthorSerializer.Meta):
        fields = AuthorSerializer.Meta.fields + ('quotes',)

    def create(self, validated_data):
        quotes = validated_data.pop('quotes', [])
        author = super().create(validated_data)

        for quote in quotes:
            Quote.objects.create(author=author, **quote)

        return author
