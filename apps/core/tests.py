# -*- coding: utf-8 -*-
import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from models import Question, Answer, UserAnswer, IMPORTANCE
from utils import get_match

class MatchTest(TestCase):
    fixtures = ['questions_answers.json']

    def test_questions_total(self):
        self.assertEqual(437, Question.objects.count())

    def test_answers_total(self):
        self.assertEqual(1189, Answer.objects.count())

    def test_answer_questions(self):
        user1, user2 = self.create_user(), self.create_user()
        self.answer_questions(user1)
        self.answer_questions(user2)
        get_match(user1, user2)

    def test_match(self):
        pass

    def create_user(self):
        random_string = "".join([ random.choice(string.ascii_lowercase) for x in xrange(10)])
        return User.objects.create_user(username=random_string, password=random_string, email=random_string+'@mail.com')

    def answer_questions(self, user):
        for q in Question.objects.all():
            if q.answers.count():
                variant = UserAnswer.objects.create(
                    user = user,
                    variant = random.choice(q.answers.all()),
                    importance = random.choice(IMPORTANCE)[0]
                )
                if variant.importance > 0:
                    variant.accepted.add(random.choice(q.answers.all()))