from test_plus import TestCase

from .quotes.factories import QuoteFactory


class HomePageTest(TestCase):

    def test_home_page(self):
        self.assertGoodView('home')

        self.assertInContext('random_quote')
        self.assertEqual(self.context['random_quote'], None)

    def test_home_page_with_quote(self):
        quote = QuoteFactory()

        self.assertGoodView('home')
        self.assertInContext('random_quote')
        self.assertEqual(self.context['random_quote'], quote)
