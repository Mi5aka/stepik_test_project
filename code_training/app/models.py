from django.db import models
from django.utils.translation import ugettext_lazy as _


class Decision(models.Model):
    evaluation = 'EV'
    correct = 'CR'
    wrong = 'WR'

    STATUSES = (
        (evaluation, _('evaluation')),
        (correct, _('correct')),
        (wrong, _('wrong'))
    )

    text = models.TextField(
        verbose_name=_('Text'),
        blank=True, null=True
    )
    status = models.CharField(
        verbose_name=_('Status'),
        max_length=2,
        choices=STATUSES,
        default=evaluation
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created datetime'),
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Decision')
        verbose_name_plural = _('Decisions')
        db_table = 'decisions'
