from django.contrib import admin

from iapp.models import User,Email,Address,Password,Confirm_Password,Propic

# Register your models here.
admin.site.register(User)
admin.site.register(Email)
admin.site.register(Address)
admin.site.register(Password)
admin.site.register(Confirm_Password)
admin.site.register(Propic)

def has_add_permission(self,request):
	if self.model.objects.count()>=1:
		return False
	return super().has_add_permission(request)