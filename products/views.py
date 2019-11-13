from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from products.src.command import create_product, vote_product
from products.src.exceptions.CustomExceptions import ProductNotExistsException
from products.src.query import detail, index
from products.src.exceptions import CustomExceptions


@require_GET
def home(request):
    query = index.Query()
    manager = index.Manager()
    products = manager(query)

    return render(request, 'products/home.html', {'products': products})


@require_GET
@login_required(login_url='show_login')
def create(request):
    return render(request, 'products/create.html')


@require_POST
@login_required(login_url='show_login')
def store_product(request):
    try:
        command = create_product.Command(request.POST.get('title'), request.POST.get('url'), request.POST.get('body'),
                                 request.FILES.get('icon'), request.FILES.get('image'), request.user)
        handler = create_product.Handler()
        handler(command)
    except ValidationError as exception:
        return render(request, 'products/create.html', {'error': exception})
    except CustomExceptions.UrlExistsException as exception:
        return render(request, 'products/create.html', {'error': exception.get_message()})
    '''except Exception as exception:
        return render(request, 'products/create.html', {'error': exception})'''
    return redirect('home')


@require_GET
def show(request, product_id):
    query_data = detail.Query(product_id)
    manager = detail.Manager()
    product = manager(query_data)
    return render(request, 'products/detail.html', {'product': product})


@require_POST
@login_required(login_url='signup')
def vote(request, product_id):
    try:
        command = vote_product.Command(product_id)
        handler = vote_product.Handler()
        handler(command)

        return redirect('product_detail', product_id=product_id)
    except ProductNotExistsException as exception:
        return redirect('product_detail', kwargs={'product_id': product_id, 'error': exception.get_message()})
