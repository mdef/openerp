# -*- coding: utf-8 -*-
from osv import fields, osv


#import sale
#import product
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

from tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, float_compare
#from datetime import datetime                                                              

class statement_property(osv.osv):
    _name = "statement.property"
    _description = "Property"
    _columns = {
        'name': fields.char('Property Name', size=128, required=True),
        'property_id': fields.many2one('statement.value', 'Statement value', select=True),
    }

statement_property()
#    def __get_next_expiration_date(self, cr, uid, ids, field_name, arg, context=None):
def _datenow(self, cursor, user_id, context=None):
    return  "22"+datetime.now()

class statement_value(osv.osv):
    _name = 'statement.value'
    _description = 'Statement Value'

    _columns = {
        'name': fields.char('Name', size=128, required=True, help=""),
        'statement_comments': fields.text('Comments'),
        'statement_datetime': fields.datetime('Date and time of statements'),
        'statement_properties': fields.one2many('statement.property', 'property_id', 'Properties'),
       # 'person_product_many': fields.many2many('product.product','product_printoptions_rel', 'person_id' , 'product_id', 'Product'),
         'product_id': fields.many2one('product.product', 'Delivery Product', required=True),
}

_defaults = {'statement_datetime': fields.datetime.now}

statement_value()

