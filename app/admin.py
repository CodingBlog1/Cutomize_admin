from django.contrib import admin
from app.models import Person, Course, Grade
from django.db.models import Avg
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "show_average")
    search_fields = ("first_name__startswith",)

    def show_average(self, obj):
        result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
        return result["grade__avg"]


# ?    show_average.short_description = "Average Grade"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "person_link")
    list_filter = ("year",)

    def person_link(self, obj):
        count = obj.person_set.count()
        url = (
            reverse("admin:app_person_changelist")
            + "?"
            + urlencode({"course__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, count)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
