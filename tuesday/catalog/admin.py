from django.contrib import admin
from .models import Contributor, Task, Board

admin.site.register(Contributor)
admin.site.register(Task)
admin.site.register(Board)
