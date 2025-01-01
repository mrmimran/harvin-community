# -*- coding: utf-8 -*-
# from odoo import http


# class HcResCompany(http.Controller):
#     @http.route('/hc_res_company/hc_res_company', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_res_company/hc_res_company/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_res_company.listing', {
#             'root': '/hc_res_company/hc_res_company',
#             'objects': http.request.env['hc_res_company.hc_res_company'].search([]),
#         })

#     @http.route('/hc_res_company/hc_res_company/objects/<model("hc_res_company.hc_res_company"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_res_company.object', {
#             'object': obj
#         })

