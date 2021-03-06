from django.contrib import admin
from .models import Testimonios

class TestimoniosAdmin(admin.ModelAdmin):
	def queryset(self, request):
		if request.user.is_superuser:
			return Testimonios.objects.all()
		return Testimonios.objects.filter(user=request.user)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

	exclude = ('user',)
	list_display = ('titulo', 'fecha', 'aprobacion', 'idioma', 'user')
	list_filter = ('idioma', 'user', 'aprobacion')
	search_fields = ('titulo',)
# Register your models here.
admin.site.register(Testimonios, TestimoniosAdmin)