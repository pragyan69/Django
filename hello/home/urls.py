from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",views.index, name  = 'home'),
     path("about" , views.about , name = "about" ),
    path("services" , views.services , name  = " services"),
     path("option1" , views.option1, name = "option1"),
     path("option2" , views.option2, name = "option2"),
     path("other_options" , views.other_options, name = "other_options")
    


]