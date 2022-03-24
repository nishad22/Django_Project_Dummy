from django.urls import path,include
from . import views
#from django.contrib import admin


#app_name = 'book_outlet'

urlpatterns = [
   path('',views.index),
   path('<slug:slug>', views.book_details,name='book-details')
    
]
