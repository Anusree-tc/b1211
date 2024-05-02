from django.shortcuts import render, get_object_or_404
from .forms import Productform
from .models import Product,Category



# Create your views here.
def home(request,slug_c=None):


    page_c=None
    products=None
    if slug_c != None:
        page_c=get_object_or_404(Category,slug=slug_c)
        products=Product.objects.all().filter(category=page_c,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,'home.html',{'category':page_c,'products':products})


def prod_det(request, slug_c, slug_p):

    try:

        product=Product.objects.get(category_slug=slug_c,slug=slug_p)
    except Exception as e:

        raise e

    return render(request,'product.html',{'product':product})


def prod_reg(request):


    if request.method =='POST':
          form=Productform(request.POST)
          if form.is_valid():
               pname=form.cleaned_data['name']
               pprice=form.cleaned_data['price']
               product=Product.objects.create(name=pname,price=pprice)
               product.save()
               return HttpResponse("Product registered succesfully")

    form=Productform()
    return render(request,'product_register.html',{'form':form})