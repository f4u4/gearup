from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from orders.models import Order

def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/inventory_list.html', {'products': products})

def update_stock(request, product_id):
    if request.method == 'POST':
        new_amount = request.POST.get('stock_amount')
        product = get_object_or_404(Product, id=product_id)
        product.stock = new_amount
        product.save()
    return redirect('inventory_list')

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        Product.objects.create(name=name, price=price, stock=stock)
        return redirect('inventory_list')

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('inventory_list')

def inventory_view(request):
    products = Product.objects.all()
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'inventory/inventory_list.html', {'products': products, 'orders': orders})

# ฟังก์ชันเปลี่ยนสถานะจัดส่ง/ยืนยันออเดอร์
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.status = request.POST.get('status')
        order.save()
    return redirect('inventory_list')

# ฟังก์ชันกดยืนยันการชำระเงิน
def confirm_payment(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        order.is_paid = True
        order.status = 'confirmed' # ปรับสถานะเป็นยืนยันออเดอร์อัตโนมัติ
        order.save()
    return redirect('inventory_list')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'inventory/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    cart[p_id] = cart.get(p_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    
    for p_id, quantity in cart.items():
        product = get_object_or_404(Product, id=p_id)
        subtotal = product.price * quantity
        total_price += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        
    return render(request, 'inventory/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('cart_detail')

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Cancelled'
    order.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))