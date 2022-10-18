from urllib import response
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Product,Review
from cart.cart import Cart

# Create your views here.
def product(request,slug):
    #product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product,slug=slug)

    cart = Cart(request)
    item = cart.get_item(product.id)
    if item:
        flag = True
    else:
        flag = False

    if request.method == 'POST':
        review = Review.objects.filter(created_by=request.user,product=product)
        rating = request.POST.get('rating',3)
        content = request.POST.get('content','') #name - default_value

        if content: 
            if review.count() > 0:
                review = review.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product = product,
                    rating = rating,
                    content = content,
                    created_by = request.user,
                )
            messages.info(request, 'Your review has been updated successfully!')
            request = render(request,'product/partials/review.html',{'product':product})
            request['hx-trigger'] = "update-review"
            return request

    #review = Review.objects.filter(product=product)
    if request.user.is_authenticated:
        review = Review.objects.filter(created_by=request.user,product=product)
        if review.count() > 0:
            review = review.first()
            response = render(request,'product/product.html',{'product':product,'review':review,'flag':flag})
            return response
        else:
            response = render(request,'product/product.html',{'product':product,'flag':flag})
            return response
    else:
        response = render(request,'product/product.html',{'product':product,'flag':flag})
        return response


def hx_update_review(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    # review = Review.objects.filter(product=product)
    # review = review.first()
    request = render(request,'product/partials/product_rating.html',{'product':product})
    return request

def hx_add_view_cart_btn(request,product_id):
    cart = Cart(request)
    item = cart.get_item(product_id)
    if item:
        flag = True
    else:
        flag = False
    return render(request,'product/partials/add_view_in_cart_btn.html',{'flag':flag})

def hx_alert_success(request):
    alert = True
    request = render(request,'product/partials/alert_success.html',{'alert':alert})
    return request