from django import forms
from .models import Book, Car

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control','style': 'width: 30rem;'}),
            'model': forms.TextInput(attrs={'class': 'form-control','style': 'width: 30rem;'}),
            'year': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 30rem;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 30rem;'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows': 5, 'cols': 20,'style': 'width: 30rem;'}),
            'image': forms.FileInput(attrs={'class': 'form-control','style': 'width: 30rem;'}),
        }
