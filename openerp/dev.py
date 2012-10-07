# -*- coding: utf-8 -*-
from osv import fields, osv


#import sale
#import product
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

from tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, float_compare
#from datetime import datetime                                                              

class dev_property(osv.osv):
    _name = "dev.property"
    _description = "Property"
    _columns = {
        'name': fields.char('Property Name', size=128, required=True),
        'property_id': fields.many2one('dev.person', 'Person Name', select=True),
    }

dev_property()



class dev_person(osv.osv):
    _name = 'dev.person'
#    _inherit = 'product.product'
    _description = 'Person'
    now = datetime.now()
    _columns = {
        'name': fields.char('Name', size=128, required=True, help=""),
       # 'product_id': fields.many2one('product.product', 'Delivery Product'),
        'person_comments': fields.text('Comments'),
        'person_datetime': fields.datetime('Date and time of statements'),
        'person_properties': fields.one2many('dev.property', 'property_id', 'Properties'),
       # 'person_product_many': fields.many2many('product.product','product_printoptions_rel', 'person_id' , 'product_id', 'Product'),
         'product_id': fields.many2one('product.product', 'Delivery Product', required=True),

 #       'person_product_id': fields.one2many(
 #                       'product.product',
 #                       'product_id',
 #                       'Product'),
    }


# _defaults = {
#     'person_datetime': fields.datetime.context_today
#         'company_id': lambda s, cr, uid, c: s.pool.get('res.company')._company_default_get(cr, uid, 'sale', context=c)
#                     }

dev_person()

