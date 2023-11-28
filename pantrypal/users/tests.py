from django.test import TestCase
from .models import Pal
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        use = User.objects.create(username="test", password="test")
        use2 = User.objects.create(username="test2", is_superuser=True)
        pal1 = Pal.objects.create(user=use, about="test")
        pal2 = Pal.objects.create(user=use2, about="test2")
        pal1.following.add(pal1)
        pal2.following.add(pal2)

    def test_get(self):
        use = User.objects.get(username="test", password="test")
        self.assertEqual(use.username, 'test')
        self.assertEqual(use.password, 'test')
        user_about = Pal.objects.get(user=use, about="test")
        self.assertEqual(user_about.about, 'test')
    def test_authenticate(self):
        use = User.objects.get(username="test", password="test")
        use2 = User.objects.get(username="test2")
        self.assertEqual(use2.is_authenticated, True)
        self.assertEqual(use.is_authenticated, True)
        self.assertEqual(use2.is_superuser, True)
        self.assertEqual(use.is_superuser, False)

    def test_add_follower(self):
        use = User.objects.get(username="test")
        use2 = User.objects.get(username="test2")
        pal1 = Pal.objects.get(user=use)
        pal2 = Pal.objects.get(user=use2)
        pal1.following.add(pal2)
        pal2.following.add(pal1)

        follow_list1 = pal1.following.all()
        follow_list2 = pal1.following.all()
        self.assertEqual(len(follow_list1), 2)
        self.assertEqual(len(follow_list2), 2)

    def test_remove_follower(self):
        use = User.objects.get(username="test")
        use2 = User.objects.get(username="test2")
        pal1 = Pal.objects.get(user=use)
        pal2 = Pal.objects.get(user=use2)
        pal1.following.remove(pal2)
        pal2.following.remove(pal1)
        follow_list1 = pal1.following.all()
        follow_list2 = pal1.following.all()
        self.assertEqual(len(follow_list1), 1)
        self.assertEqual(len(follow_list2), 1)

    def test_not_following(self):
        use = User.objects.get(username="test")
        pal1 = Pal.objects.get(user=use)
        follow_list = pal1.following.all()
        unfollowed_list = Pal.objects.exclude(pk__in=follow_list.values_list('pk', flat=True))
        self.assertEqual(len(unfollowed_list), 1)
