from app import  db
from modules.products.model import Producto

def agregar_producto():
    # Crear un nuevo producto manualmente
    nuevo_producto = Producto(
        name='Producto de prueba',
        description='Descripción del producto de prueba',
        price=99.99,
        image_url='http://example.com/imagen.jpg'
    )
    print(nuevo_producto)
    # Agregar el producto a la sesión y guardar los cambios
    db.session.add(nuevo_producto)
    db.session.commit()
    print('Producto agregado exitosamente.')