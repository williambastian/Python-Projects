from django.db import models


# create model of university classes
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # create model manager
    object = models.Manager()

    # display object output values in string format
    def __str__(self):
        # return input value of title and instructor name fields as tuple,
        # to display in browser instead of default values
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # remove added 's' that Django adds to model name in browser display
    class Meta:
        verbose_name_plural = "University Classes"
