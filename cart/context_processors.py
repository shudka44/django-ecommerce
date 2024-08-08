from .cart import Cart

# Create context processors can work on all pages
def cart(request):
    # Return the default data from our cart
    return {'cart': Cart(request)}
