class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, recetas):
        if str(recetas.id) not in self.cart.keys():
            self.cart[recetas.id] = {
                "recetas_id": recetas.id,
                "nombre_receta": recetas.nombre_receta,
                "quantity": 1,
                "precio_receta": str(recetas.precio_receta),
                "image": recetas.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(recetas.id):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.save()
        
        
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
        
    
    def remove(self, recetas):
        recetas_id = str(recetas.id)
        if recetas_id in self.cart:
            del self.cart[recetas_id]
            self.save()
            
    
    def decrement(self, recetas):
        for key, value in self.cart.items():
            if key == str(recetas.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(recetas)
                self.save()
                break
            else:
                print("El producto no existe en el carrito")
    
    
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True