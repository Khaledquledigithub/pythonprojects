"""profproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from iapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("log",views.logview),

    path("form/",views.form_view),
    path("profile/",views.home_view),
    path("eform/",views.eform_view),
    path("pform/",views.pform_view),
    path("cform/",views.cform_view),
    path("aform/",views.aform_view),
    path("piform/",views.piform_view),
    path("delete/<int:id>",views.del_user),
    path("delete1/<int:id>",views.del_email),
    path("delete2/<int:id>",views.del_add),
    path("update/<int:id>",views.up_view),
    path("update1/<int:id>",views.upe_view),
    path("update2/<int:id>",views.upa_view),

]
if settings.DEBUG:
	urlpatterns+static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)
