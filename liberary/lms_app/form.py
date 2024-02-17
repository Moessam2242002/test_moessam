from django import forms
from .models import *
class CtegoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
class update_book(forms.ModelForm):
    class Meta:
        model=Books
        fields=['book_name','auther','book_image','auther_image','pages','price','rental_price_day','rental_period','total_rental','status','category']
        widgets={
        'book_name': forms.TextInput(attrs={'class':'form-control'}),
        'auther':forms.TextInput(attrs={'class':'form-control'}),
        'book_image':forms.FileInput(attrs={'class':'form-control'}),
        'auther_image':forms.FileInput(attrs={'class':'form-control'}),
        'pages':forms.NumberInput(attrs={'class':'form-control'}),
        'price':forms.NumberInput(attrs={'class':'form-control'}),
        'rental_price_day':forms.NumberInput(attrs={'class':'form-control','id':"rental_price"}),
        'rental_period':forms.NumberInput(attrs={'class':'form-control','id':"rental_period"}),
        'total_rental':forms.NumberInput(attrs={'class':'form-control','id':"total_rental"}),
        'status':forms.Select(attrs={'class':'form-control'}),
        'category':forms.Select(attrs={'class':'form-control'}),
        }