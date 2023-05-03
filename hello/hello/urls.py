
from django.contrib import admin
from django.urls import path,include
from home import views
admin.site.site_header = "prantu boss of the world"
admin.site.site_title = "prantu boss Portal"
admin.site.index_title = "welcome to the boss Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('home.urls'))
    # path("",views.index, name  = 'home'),
    #  path("about" , views.about , name = "about" ),
    # path("services" , views.services , name  = " services")
    
    
]
