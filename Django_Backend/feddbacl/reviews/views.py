#from urllib import request
from email.mime import base
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView

# Create your views here.

# class ReviewView(View):
    
    
#     def get(self,request):
#         form  = ReviewForm()
        
#         return render(request,'reviews/review.html',{
#         'form':form
#         })
    
    
#     def post(self,request):
#         form  = ReviewForm(request.POST)   
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request,'reviews/review.html',{
#         'form':form
#         })

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html' #take care of get and post method
    success_url = '/thank-you'

    #it will execute when Django save data  
    def form_valid(self, form):
        form.save() #this svae data to database 
        return super().form_valid(form)

# class ThankYouView(View):
#     def get(self,request):
#         return render(request,'reviews/thank_you.html')

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['message']= 'This works'
        return context

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review 
    #the above code will run. However, in review_list.html the name of object will be 'object_list' by default
    #in order to customize the object name to 'reviews' we are using below code
    #variable name can be anything
    context_name = 'reviews'

    def get_queryset(self):
        base_query =  super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return data
    

    
    #below code is for TemplateView
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context

class SingleReviewView(DetailView):
    template_name = 'reviews/single_view.html'
    #it will load all model Review data into attribute
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        #context['is_favorite'] = True
        return context


    #below code is for TemplateView
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id =  kwargs['id']
    #     selected_review = Review.objects.get(pk = review_id)
    #     context['review'] = selected_review
    #     return context

#Sessions

class AddFavoriteView(View):
    def post(self,request): 
        review_id =  request.POST['review_id']
        #fav_review =  Review.objects.get(pk = review_id)
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/'+review_id)



# def review(request):
#     # if  request.method =='POST':
#     #     entered_username = request.POST['name']

#     #     if entered_username == '':
#     #         return render(request, 'reviews/review.html',{
#     #             'has_error': True
#     #         })
#     #     print(entered_username)
#     #     return HttpResponseRedirect("/thank-you")

    # # return render(request,'reviews/review.html',{
    # #     'has_error':False
    # # })

    # if  request.method =='POST':    
    #     #existing_data = Review.objects.get(pk=1)
    #     #form = ReviewForm(request.POST,instance=existing_data)
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         # review = Review(user_name = form.cleaned_data['user_name'],
    #         #                 review_text = form.cleaned_data['review_text'],
    #         #                 rating=form.cleaned_data['rating'])
    #         # review.save()
    #         # print(form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    
    # else:
    #     form  = ReviewForm()
        
    # return render(request,'reviews/review.html',{
    #     'form':form
    # })


# def thank_you(request):
#     return render(request,'reviews/thank_you.html')
