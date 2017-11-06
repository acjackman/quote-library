from test_plus.test import TestCase

from .factories import AuthorFactory
from quotelibrary.users.factories import StaffFactory


class AuthorViewTestCase(TestCase):

    def setUp(self):
        self.author = AuthorFactory()


class TestAuthorDetailView(AuthorViewTestCase):

    def test_view_author(self):
        self.assertGoodView('authors:detail', pk=self.author.pk)


class TestAuthorListView(AuthorViewTestCase):

    def test_list_no_authors(self):
        self.author.delete()
        response = self.assertGoodView('authors:list')
        self.assertInContext('object_list')
        obj_list = response.context_data['object_list']
        self.assertEqual(len(obj_list), 0)

    def test_list_one_author(self):
        response = self.assertGoodView('authors:list')
        self.assertInContext('object_list')
        obj_list = response.context_data['object_list']
        self.assertEqual(len(obj_list), 1)

    def test_list_five_authors(self):
        authors = []
        for i in range(4):
            authors.append(AuthorFactory())
        response = self.assertGoodView('authors:list')
        self.assertInContext('object_list')
        obj_list = response.context_data['object_list']
        self.assertEqual(len(obj_list), 5)


class AuthorModifyViewTestCase(AuthorViewTestCase):

    def setUp(self):
        self.staff_user = StaffFactory(password='password')
        super(AuthorModifyViewTestCase, self).setUp()


class TestAuthorCreateView(AuthorModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('authors:create')
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('authors:create')


class TestAuthorUpdateView(AuthorModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('authors:update', pk=self.author.pk)
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('authors:update', pk=self.author.pk)


class TestAuthorDeleteView(AuthorModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('authors:delete', pk=self.author.pk)
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('authors:delete', pk=self.author.pk)


class TestAuthorQuoteCreateView(AuthorModifyViewTestCase):

    def test_annon_user_blocked(self):
        response = self.get('authors:newquote', pk=self.author.pk)
        self.response_302(response)

    def test_staff_user_acccess(self):
        with self.login(username=self.staff_user.username):
            self.assertGoodView('authors:newquote', pk=self.author.pk)
