from django.contrib import admin
from .models import Questions, Friendship, UserProfile, QuestionsVerbal1, QuestionsVerbal2, QuestionsVerbal3, QuestionsMath1
# Register your models here.

admin.site.register(Questions)
admin.site.register(Friendship)
admin.site.register(UserProfile)
admin.site.register(QuestionsVerbal1)
admin.site.register(QuestionsVerbal2)
admin.site.register(QuestionsVerbal3)
admin.site.register(QuestionsMath1)
