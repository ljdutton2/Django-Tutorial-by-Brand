from django.contrib import admin


from .models import Question

admin.site.register(Question)
# Register your models here.
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra  = 3

class QuestionAdmin(admin)