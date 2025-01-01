# -*- coding: utf-8 -*-
# from odoo import http


# class HcResPartner(http.Controller):
#     @http.route('/hc_res_partner/hc_res_partner', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_res_partner/hc_res_partner/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_res_partner.listing', {
#             'root': '/hc_res_partner/hc_res_partner',
#             'objects': http.request.env['hc_res_partner.hc_res_partner'].search([]),
#         })

#     @http.route('/hc_res_partner/hc_res_partner/objects/<model("hc_res_partner.hc_res_partner"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_res_partner.object', {
#             'object': obj
#         })

