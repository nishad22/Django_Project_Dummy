from django.urls import reverse
from cgitb import text
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render # here render can be used in place render_to_string function mostly using for template    
from django.template.loader import render_to_string
# Create your views here.

# def jan(request):
#     return HttpResponse("January") #constructor function

# def feb(rquest):
#     return HttpResponse("February") #constructor function

monthly_challenges = {
    'january' : 'this is 1st month of year',
    'february': 'this is 2nd month of year',
    'march' : 'this is 3rd month of year',
    'april' : 'this is 4th month of year',
    'may' : 'this is 5th month of year',
    'june' : 'this is 6th month of year',
    'july' : 'this is 7th month of year',
    'august' : None
}




#below is the code for dyanmic view. Below are the severral ways to do it
# Note: The second argument we passed in function must be same as argumnt we pass in path function in placeholder--> <> in urls.py filr
# Note: the function mention here should be in same name as path mention in urls.py

def monthly_challenge_by_number(request, month): #using concepts of redirect

    # HttpResponseRedirect is a subclass of HttpResponse (source code) in the Django web framework 
    # that returns the HTTP 302 status code,indicating the URL resource was found but temporarily moved to a different URL. 
    # This class is most frequently used as a return object from a Django view.

    #we are using dictionary function key() to get list of value representing key in dictionary  
    # then using list() to convert it into  proper list
    month_list =  list(monthly_challenges.keys())
    if month > len(month_list):
        return HttpResponseNotFound('Month not found 404')
    redirect_month =    month_list[month-1]
    redirect_path = reverse('month_challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
   
# below code is accepting month as string
# def monthly_challenge(request, month):
#     try:
#         text = monthly_challenges[month]
#         text_data = f"<h1>{text}</h1>"
#     except:
#         return HttpResponseNotFound('Month not found 404')
#     return HttpResponse(text_data)

#static HTML code
# def monthly_challenge(request, month):
#      try:
#          text = monthly_challenges[month]
#          # below render_to_string is working because we have template in monthly_challenges/setting.py 
#          text_data = render_to_string('challenges/challenge.html')
#      except:
#          return HttpResponseNotFound('Month not found 404')
#      return HttpResponse(text_data)

# below code shows that we can make our code more dynamic 
#below I am using render function so that I can use template
def monthly_challenge(request, month):
     try:
         text_data = monthly_challenges[month]
         # in below function our first argument would be the first argument of monthly_challenge function which is "request"
         return render(request,'challenges/challenge.html',{ 
            'text' : text_data,
            'month_name' : month.capitalize()
            })
     except:
         return HttpResponseNotFound('Month not found 404')
     

 
#create HTML view 

# def index(request):
#     list_items = ""
#     months_list = list(monthly_challenges.keys())
#     for month in months_list:
#         month_path = reverse('month_challenge',args = [month]) #challenges/month
#         list_items += f"<li><a href =\"{month_path}\">{month.capitalize()}</a></li>"
    
#     response_data = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_data)

# In below code, I am gonna do the same as above code but in challenge.html by using tags

def index(request):
    months_list = list(monthly_challenges.keys())
    return render(request,'challenges/index.html',{
        'months': months_list
         })



# In below code we are using if else statements to make more dynamic
# def monthly_challenge(request, month):
#     text = ''
#     if month == 'january':
#         text = 'this is 1st month of year'
#     elif month == 'february':
#         text = 'this is 2nd month of year'
#     elif month == 'march':
#         text = 'this is 3rd month of year'
#     elif month == 'april':
#         text = 'this is 4th month of year'
#     elif month == 'may':
#         text = 'this is 5th month of year'
#     else:
#         return HttpResponseNotFound('Response not found')
#     return HttpResponse(text)