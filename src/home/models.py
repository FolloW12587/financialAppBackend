from django.db import models

# Create your models here.


class SupportTicket(models.Model):
    """ Модель обращения в службу поддержки """
    OPENED = "0"
    PROCESSING = "1"
    CLOSED = "2"
    STATUS_CHOICES = (
        (OPENED, "opened"),
        (PROCESSING, "processing"),
        (CLOSED, "closed")
    )

    id = models.AutoField("id", primary_key=True)
    username = models.CharField("Имя пользователя", max_length=127)
    email = models.EmailField("Почта пользователя", max_length=127)
    text = models.TextField("Текст обращения")
    status = models.CharField("Статус обращения", max_length=2, choices=STATUS_CHOICES, default=OPENED, editable=False)
    time_opened = models.DateTimeField("Время открытия", auto_now_add=True)
    time_closed = models.DateTimeField("Время закрытия", blank=True, null=True, editable=False)

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"

    def __str__(self):
        return self.email