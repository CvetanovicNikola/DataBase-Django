
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("search.html/", views.search, name="search"),
    path("insert/", views.insert, name="insert"),
    path("insert.html/", views.insert, name="insert"),
    path('admin/', admin.site.urls, name="admin"),
    #path("lastname/", views.get_lastname),
    path("all_employees.html", views.view_all_employees, name="view_all"),
    path('employee.html', views.get_lastname, name='get_name'),
    path('employee.html/<lastname>', views.get_employee, name='employee_detail')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
