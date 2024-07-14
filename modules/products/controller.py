from __main__ import app
from flask import Flask, render_template 
from modules.products.model import Producto


    
@app.route('/lista_productos')
def product_list():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Producto.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)   