#from cProfile import label
#from distutils.log import error
#from typing_extensions import Required
from django import forms
from .models import Review 

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your Name', max_length=50, error_messages = {
#        'required':'Your name must not empty',
#        'max_length':'Please enter shorter name'
#     })
#     review_text = forms.CharField(label = 'Your Feedback',widget=forms.Textarea,max_length = 200)
#     rating = forms.IntegerField(label='Your Rating',min_value=1,max_value=5)

#Modelsform

class ReviewForm(forms.ModelForm):
   class Meta:
      model = Review
      #below line will render all field from form
      fields = '__all__'
      #below will exclude field from form
      #exclude  = ['owner comment]
      #customize the labels of form fields
      label = {
         'user_name' : 'Your Name',
         'review_text' : 'Your Feedback',
         'rating' : 'Your Rating'
      }
      error_messages = {
         'user_name':{
            'required':'Your name must not empty',
            'max_length':'Please enter shorter name'
         } 
      }