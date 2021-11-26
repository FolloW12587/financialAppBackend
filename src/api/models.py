from django.db import models
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
    fin_type = models.ForeignKey(FinancailUnitsType, verbose_name="Тип", on_delete=models.CASCADE)
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
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

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