from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    campusName = models.CharField(max_length=60, default="", blank=True, null=False)
    stateName = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    # display object output values in string format
    def __str__(self):
        display_campus = '{0.campusName}: {0.stateName}'
        return display_campus.format(self)

    class Meta:
        verbose_name = "University Campus"
        verbose_name_plural = "University Campus"
