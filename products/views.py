from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone
#from django.views.generic import TemplateView

def home(request):
    Product = product.objects
    return render(request, 'products/home.html', {'Product':Product })

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and  request.POST['body']and request.FILES['image'] and request.FILES['icon'] and request.POST['url']:
            Product = product()
            Product.title = request.POST['title']
            Product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Product.url = request.POST['title']
            else:
                Product.url = 'http://' + request.POST['url']
            Product.icon = request.FILES['icon']
            Product.image = request.FILES['image']
            #print(uploaded_image.name)
            #print(uploaded_icon.name)
            Product.pub_date = timezone.datetime.now()
            Product.hunter = request.user
            Product.save()
            return redirect('/products/'+ str(Product.id))
            
        else:
            return render(request, 'products/create.html', {'error':'please fill out all the fields'})
        
    else:    
        return render(request, 'products/create.html')


def detail(request, product_id):
    Product = get_object_or_404(product, pk=product_id)
    return render(request, 'products/detail.html', {'Product':Product})

@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        Product = get_object_or_404(product, pk=product_id)
        Product.votes_total +=1
        Product.save()
        return redirect('/products/'+ str(Product.id))
















