from django.db import models

# Create your models here.



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
    description = models.TextField("Описание", null=True, blank=True)
    short_description = models.CharField("Короткое описание", max_length=255, blank=True, null=True)
    range_str = models.CharField("Диапазон", max_length=255, blank=True, null=True)
    active = models.BooleanField("Активно", default=True)
    link = models.TextField("Ссылка")

    class Meta:
        verbose_name = "Финансовая единица"
        verbose_name_plural = "Финансовые единицы"
        
    def __str__(self):
        return self.name