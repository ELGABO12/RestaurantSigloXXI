from django.conf import settings
from apps.mantenedor.models import Receta


class Cart(object):
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, receta, cantidad=1):
        receta_id = str(receta.id)
        if receta_id not in self.cart:
            self.cart[receta_id] = {
                "recetas_id": receta.id,
                "nombre_receta": receta.nombre_receta,
                "cantidad": 1,
                "precio_receta": str(receta.precio_receta),
                "image": receta.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(receta.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()
        
        
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
        
    
    def remove(self, receta):
        receta_id = str(receta.id)
        if receta_id in self.cart:
            del self.cart[receta_id]
            self.save()
            
    def __iter__(self):
        receta_ids = self.cart.keys()
        recetas = Receta.objects.filter(id__in=receta_ids)
        for receta in recetas:
            self.cart[str(receta.id)]['receta'] = receta
        
        for item in self.cart.values():
            item['precio_receta'] = float(item['precio_receta'])
            item['precio_total'] = item['precio_receta'] * item['cantidad']
            yield item
            
    
    def __len__(self):
        return sum(item['cantidad'] for item in self.cart.values())
    
    
    def get_total_price(self):
        return sum(float(item['precio_receta']) * item['cantidad'] for item in self.cart.values())
    
    
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