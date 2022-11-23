def total_carrito(request):
    total = 0.0 
    if request.user.is_authenticated:

        if 'cart' in request.session:
            for key,value in request.session['cart'].items():
                total = total +(float(value['precio_receta'])*value['quantity'])

    return {'total_carrito':total}