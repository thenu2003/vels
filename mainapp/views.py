from django.shortcuts import render, redirect

def store(request):
	context = {}
	return render(request, 'store.html', context)

def cart(request):
	context = {}
	return render(request, 'cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'checkout.html', context)

def order(request):

    context = {
        'message': 'Order purchased successfully!',
        'thank_you_message': 'Thank you for your purchase. Your order has been successfully processed.'
    }
    return render(request, 'order.html', context)
