# -*- coding: utf-8 -*-
# from odoo import http


# class Managealvaro(http.Controller):
#     @http.route('/managealvaro/managealvaro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managealvaro/managealvaro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managealvaro.listing', {
#             'root': '/managealvaro/managealvaro',
#             'objects': http.request.env['managealvaro.managealvaro'].search([]),
#         })

#     @http.route('/managealvaro/managealvaro/objects/<model("managealvaro.managealvaro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managealvaro.object', {
#             'object': obj
#         })
