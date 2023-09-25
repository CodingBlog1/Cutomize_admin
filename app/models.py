from django.db import models
from django.core import validators

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    coures = models.ManyToManyField("Course", blank=True)

    class Meta:
        ordering = ("first_name", "last_name")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=1000)
    year = models.IntegerField()

    class Meta:
        unique_together = (
            "name",
            "year",
        )

    def __str__(self):
        return f"{self.name}, {self.year}"


class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)]
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade}, {self.person}, {self.course}"
