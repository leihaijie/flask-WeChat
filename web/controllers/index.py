# -*- coding: utf-8 -*-
from application import app,db
from flask import Blueprint
from common.libs.Helper import ops_render
from common.models.food.FoodSaleChangeLog import FoodSaleChangeLog
from common.models.pay.PayOrder import PayOrder
from common.models.member.Member import Member



route_index = Blueprint( 'index_page',__name__ )

@route_index.route("/")
def index():
    resp_data = {
        'data':{
            'finance':{
                'today':0
            },
            'member': {
                'total': 0
            },
            'order': {
                'today': 0
            },
            'shared': {
                'today': 0
            },
        }
    }
    query = FoodSaleChangeLog.query
    food_finance = query.all()
    finance = 0
    for item in food_finance:
        price = item.quantity * item.price
        finance += price

    query = PayOrder.query
    order = query.filter(PayOrder.status == 1, PayOrder.express_status == 1, PayOrder.comment_status == 1).count()

    query  = Member.query
    member = query.count()

    app.logger.info(member)

    data = resp_data['data']
    data['finance']['today'] = finance
    data['order']['today'] = order
    data['member']['total'] = member
    return ops_render( "index/index.html",resp_data )