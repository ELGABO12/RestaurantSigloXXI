def total_carrito(request):
    total = 0.0 
    if not request.user.is_authenticated or request.user.is_authenticated:

        if 'cart' in request.session:
            for key,value in request.session['cart'].items():
                total = total +(float(value['precio_receta'])*value['cantidad'])

    return {'total_carrito':total}