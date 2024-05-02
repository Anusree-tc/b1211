from django import forms


class Productform(forms.Form):
    name=forms.CharField(max_length=100,label="Enter the name of  the product")
    price=forms.IntegerField(label="Enter the price")