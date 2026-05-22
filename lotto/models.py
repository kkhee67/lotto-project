from django.db import models


class LottoTicket(models.Model):

    numbers = models.CharField(max_length=100)

    result = models.CharField(
        max_length=20,
        default='미추첨'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numbers