import time
import hashlib
from celery import shared_task
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

from .models import Decision
from .emulator import post_submission, get_submission


def check_cache_result(text):
    hash_text = hashlib.md5(text.encode())
    return cache.get(hash_text.hexdigest())


def create_cache_result(text, status):
    hash_text = hashlib.md5(text.encode())
    cache.set(hash_text.hexdigest(), status)


def check_status(text):
    # если нет решения в кеше, то делаем первый запрос к post_submission
    # если сразу получили решение, то сохраняем его и кешируем
    id, status = post_submission(text)
    if status in ('wrong', 'correct'):
        return status

    # в реальной ситуации использование while было довольно плохим решением
    # но в нынешней ситуации это более простое решение
    while status == 'evaluation':
        id, status = get_submission(id)
        time.sleep(1)

    # кешируем ответ
    create_cache_result(text, status)
    return status


@shared_task
def task_check_results(id):
    try:
        decision = Decision.objects.get(id=id)
        status = check_status(decision.text)
        decision.status = getattr(Decision, status)
        decision.save(update_fields=['status'])
    except ObjectDoesNotExist:
        return ObjectDoesNotExist

