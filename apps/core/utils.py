# -*- coding: utf-8 -*-
from models import UserAnswer, Question

def get_match(user1, user2):
    calc = {
        'match': {'count': 0, 'value': 0},
        'friend': {'count': 0, 'value': 0},
        'enemy': {'count': 0, 'value': 0},
    }
    same_questions = get_same_questions(user1, user2)

    for q in same_questions:
        user1_answer = user1.answers.filter(variant__question = q)
        user2_answer = user2.answers.filter(variant__question = q)

        if not user1_answer.count() or not user2_answer.count():
            continue
        else:
            user1_answer = user1_answer[0]
            user2_answer = user2_answer[0]

        if user1_answer.variant == user2_answer.variant:
            k = 1
        elif user2_answer.accepted.filter(id = user1_answer.variant.id).count() and user1_answer.accepted.filter(id = user2_answer.variant.id).count():
            k = 0.5
        else:
            calc['friend']['value'] -= 0.01
            calc['match']['value'] -= 0.1
            k = -1

        m = k*0.25*abs(user1_answer.importance - user2_answer.importance)

        if m < -0.5:
            calc['enemy']['count'] += 1
            calc['enemy']['value'] += abs(m)
        if -0.5 <= m <= 0.5:
            calc['friend']['count'] += 1
            calc['friend']['value'] += (m + 0.5)
        if 0.5 < m:
            calc['match']['count'] += 1
            calc['match']['value'] += m

    result = dict()

    for key, value in calc.items():
        result[key] = "%1.2f" % round(value['value']/value['count'], 2)

    print result

def get_same_questions(user1, user2):
    same_questions = Question.objects.raw("""SELECT * FROM core_question
        JOIN core_answer ON core_question.id = core_answer.question_id
        JOIN core_useranswer ON core_answer.id = core_useranswer.variant_id
        WHERE core_useranswer.user_id IN (%s, %s)""", params=[user1.pk, user2.pk])
    return same_questions

