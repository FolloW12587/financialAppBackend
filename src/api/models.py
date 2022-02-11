import re
from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q


class FinancailUnitsType(models.Model):
    """ Типы финансовых единиц """
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("Наименование", max_length=127)

    class Meta:
        verbose_name = "Тип финансовой единицы"
        verbose_name_plural = "Типы финансовых единиц"

    def __str__(self):
        return self.name


class FinancialUnit(models.Model):
    """ Финансовая единица """
    id = models.AutoField("id", primary_key=True)
    fin_type = models.ForeignKey(
        FinancailUnitsType, verbose_name="Тип", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=255)

    loan_terms = models.TextField("Условия займа")
    requirements = models.TextField("Требования")

    sum = models.CharField("Сумма", max_length=255)
    term = models.CharField("Срок", max_length=255)
    bid = models.CharField("Ставка", max_length=255)

    rating = models.FloatField("Рейтинг",
                               validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    active = models.BooleanField("Активно", default=True)
    link = models.TextField("Ссылка")
    image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = "Финансовая единица"
        verbose_name_plural = "Финансовые единицы"

        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(rating__gte=0.0) & Q(rating__lte=5.0),
                name='financialunit_rating_range'),
        )

    def __str__(self):
        return self.name


class Settings(models.Model):
    """ Настройки для приложения / фронта """
    INT = 'int'
    DOUBLE = 'dbl'
    STRING = 'str'
    LIST = 'lst'
    SETTINGS_TYPE_CHOICES = (
        (INT, 'integer'),
        (DOUBLE, 'double'),
        (STRING, 'string'),
        (LIST, 'array')
    )
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("Наименование", max_length=31,
                            help_text="Имя настройки, только латинские буквы")
    desc = models.CharField("Описание", max_length=255, null=True, blank=True)
    settings_type = models.CharField("Тип", max_length=3, choices=SETTINGS_TYPE_CHOICES,
                                     help_text="Десятичная часть в типе Double разделяется точкой (.) . Массив Array интерпретируется как список строк, каждый элемент которого разделен запятой.")
    value = models.CharField("Значение", max_length=255)

    def clean(self) -> None:
        if re.search(r"[^A-Za-z]", self.name):
            raise ValidationError({"name": "Name contains forbidden characters"})

        if self.settings_type == self.INT:
            try:
                int(self.value)
            except:
                raise ValidationError({'value': "Can't convert given value into integer"})
        elif self.settings_type == self.DOUBLE:
            try:
                float(self.value)
            except:
                raise ValidationError({'value': "Can't convert given value into double"})

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.name


class LeadFormData(models.Model):
    """ Данные с лидформы """
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("Название", max_length=255)
    email = models.CharField("Почта", max_length=255)
    phone = models.CharField("Телефон", max_length=31)
    sum = models.DecimalField("Сумма", max_digits=6, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = "Данные с лид формы"
        verbose_name_plural = "Данные с лид формы"

    def __str__(self):
        return self.name