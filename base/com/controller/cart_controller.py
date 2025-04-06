from flask import Flask, render_template, request, redirect, url_for,session

from base.com.dao.cart_dao import CartDAO
from base.com.dao.user_register_dao import UserRegisterDAO


from base.com.vo.user_register_vo import UserRegisterVO
from base.com.vo.cart_vo import CartVO

import os
from base import app

@app.route('/user/add_cart', methods=['POST'])
def add_cart():
    cart_dao = CartDAO()
    cart_vo = CartVO()

    user_id = session.get('user_id')
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    try:
        quantity = int(quantity)
        price = int(price)
        total_price = quantity * price
    except ValueError:
        return "Invalid quantity or price", 400

    update_cart_item = cart_dao.get_cart_item(user_id, product_id)
    if update_cart_item:
        new_quantity = quantity + update_cart_item.quantity
        new_price = price * new_quantity

        cart_vo.cart_id = update_cart_item.cart_id
        cart_vo.user_id = user_id
        cart_vo.product_id = product_id
        cart_vo.price = price
        cart_vo.quantity = new_quantity
        cart_vo.total_price = new_price

        cart_dao.mearge_cart(cart_vo)
    else:
        cart_vo.user_id = user_id
        cart_vo.product_id = product_id
        cart_vo.quantity = quantity
        cart_vo.price = price
        cart_vo.total_price = total_price
        cart_dao.add_cart(cart_vo)

    return redirect(request.referrer)

@app.route('/user/view_cart')
def view_cart():
    cart_dao = CartDAO()

    user_id = session.get('user_id')
    user_cart_data = cart_dao.get_cart_data(user_id)
    return render_template('user/cart.html',user_cart_data=user_cart_data)

@app.route('/user/delete_cart_item')
def delete_cart():
    cart_dao = CartDAO()
    cart_id = request.args.get('cart_id')
    cart_dao.delete_cart(cart_id)
    return redirect('/user/view_cart')

@app.route('/user/delete_all_cart_item')
def delete_all_cart_item():
    cart_dao = CartDAO()
    user_id = session.get('user_id')
    cart_dao.delete_cart_all_item(user_id)
    return redirect('/user/view_cart')
