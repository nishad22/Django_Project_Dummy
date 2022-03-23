from django.urls import path
from . import views #importing data from views file within same folder Challenges

#I am not writng here challenges/January because In main folder monthy_challenges we are importing this urls
#path('challenges/',include('challenges.urls')) which automtically accepts in this format challenges/January


urlpatterns = [
#Below code is for calling individual view
# path('january',views.jan),
# path('february',views.feb)

#below code is for calling dynamic view i.e based on value of view the URL will be selected accordingly
# <>-->place holder which take value/input from selected view
    path('',views.index, name = 'index'),
    path('<int:month>',views.monthly_challenge_by_number),
    path('<str:month>',views.monthly_challenge,name = 'month_challenge'),
    
]