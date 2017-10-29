from api.serializers import CreateAuthorSerializer


class TestCreateAuthorSerializer:

    def test_creating_author_without_quotes(self, mocker):
        author_create = mocker.patch('api.serializers.Author.objects.create')

        data = {
            'last_name': 'Yoda'
        }

        lizr = CreateAuthorSerializer(data=data)
        assert lizr.is_valid(), lizr.errors
        lizr.save()

        author_create.assert_called_with(**data)

    def test_creating_author_with_quote(self, mocker):
        author_create = mocker.patch('api.serializers.Author.objects.create')
        quote_create = mocker.patch('api.serializers.Quote.objects.create')

        author = {
            'last_name': 'Yoda',
        }
        quotes = [
            {'text': 'Do or do not, there is no try.'},
        ]
        data = {
            'quotes': quotes,
            **author,
        }

        lizr = CreateAuthorSerializer(data=data)
        assert lizr.is_valid(), lizr.errors
        saved_author = lizr.save()

        author_create.assert_called_with(**author)
        quote_create.assert_called_with(author=saved_author, **quotes[0])

    def test_creating_author_with_quotes(self, mocker):
        author_create = mocker.patch('api.serializers.Author.objects.create')
        quote_create = mocker.patch('api.serializers.Quote.objects.create')

        author = {
            'last_name': 'Yoda',
        }
        quotes = [
            {'text': 'Do or do not, there is no try.'},
            {'text': 'Truly wonderful, the mind of a child is.'},
        ]
        data = {
            'quotes': quotes,
            **author,
        }

        lizr = CreateAuthorSerializer(data=data)
        assert lizr.is_valid(), lizr.errors
        lizr.save()

        author_create.assert_called_with(**author)
        assert quote_create.call_count == 2
