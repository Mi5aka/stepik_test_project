import hashlib
from celery import shared_task
from django.core.cache import cache

from .models import Decision
from .emulator import post_submission, get_submission


def check_cache_result(text):
    hash_text = hashlib.md5(text.encode())
    return cache.get(hash_text.hexdigest())


def create_cache_result(text, status):
    hash_text = hashlib.md5(text.encode())
    cache.set(hash_text.hexdigest(), status)

@shared_task
def task_check_results(id):
    decision = Decision.objects.get(id=id)
    # проверяем есть ли решение в кеше?
    status = check_cache_result(decision.text)
    if status:
        # если решение есть, то просто возвращаем его
        decision.status = getattr(Decision, status)
        decision.save()
        return decision.id, decision.status
    # если нет решения в кеше, то делаем первый запрос к post_submission
    # если сразу получили решение, то сохраняем его и кешируем
    id, status = post_submission(decision.text)
    if status in ('wrong', 'correct'):
        # TODO: вынести в отдельный метод кеширование
        decision.status = getattr(Decision, status)
        decision.save()
        # кешируем первый ответ
        create_cache_result(decision.text, status)
        return decision.id, decision.status

    # TODO: написать асинхронный вызов get_submission
    while status == 'evaluation':
        id, status = get_submission(id)
    decision.status = getattr(Decision, status)
    decision.save()
    # кешируем ответ
    create_cache_result(decision.text, status)
    return decision.id, decision.status

