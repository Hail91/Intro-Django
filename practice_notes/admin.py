# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Note, PersonalNote

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = (id,)

admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)
