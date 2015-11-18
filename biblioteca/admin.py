from django.contrib import admin
from .models import Biblioteca, Documentales, Audios, Adjuntos


class DocumentalesInline(admin.TabularInline):
    model = Documentales
    extra = 1


class AudioInline(admin.TabularInline):
    model = Audios
    extra = 1


class AdjuntosInline(admin.TabularInline):
    model = Adjuntos
    extra = 1


class BibliotecaAdmin(admin.ModelAdmin):
    inlines = [DocumentalesInline, AudioInline, AdjuntosInline]
    list_display = ('titulo', 'palabras_claves', 'user')


# Register your models here.
admin.site.register(Biblioteca, BibliotecaAdmin)