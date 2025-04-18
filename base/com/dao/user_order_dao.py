from base import db

from base.com.vo.user_order_vo import OrderVO
from base.com.vo.user_order_item_vo import OrderItemVO
from base.com.vo.product_vo import ProductVO

class OrderDAO:

    def view_order(self,user_id):
        order_data = db.session.query(ProductVO, OrderVO,OrderItemVO).join(OrderItemVO,OrderVO.order_id==OrderItemVO.order_id).join(ProductVO,OrderItemVO.product_id==ProductVO.product_id).filter(OrderVO.user_id==user_id).all()
        return order_data