from django.shortcuts import render , redirect
from .models import Product
from django.utils import timezone

## this for give authentication to logged in user only
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request , 'products/home.html')


## view for create a product
@login_required
## this decoration from import fo2
## 3shan m7dsh 8er el loggedin user bs ele y2der yd5ol 3la sf7t el create
def create(request):

    #check if the request is POST ?!
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] :
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            ## check if url request include http request or not
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
                product.icon = request.FILES['icon']
                product.image = request.FILES['image']
                product.pub_date = timezone.datetime.now()
                product.hunter = request.user
                product.save() ## to save at database
                return redirect('home')

        else:
            return render(request , 'products/create.html',{'error':'All Fields Are Required'})
    else:
        return render(request , 'products/create.html')
