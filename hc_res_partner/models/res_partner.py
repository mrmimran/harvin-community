from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    building_no = fields.Char(store=True, readonly=False, string='Building No')
    additional_no = fields.Char(store=True, readonly=False, string='Additional No')
    other_seller_id = fields.Char(store=True, readonly=False, string='Other Seller Id')
    arabic_name = fields.Char('Arabic Name')
    arabic_street = fields.Char('Street')
    arabic_street2 = fields.Char('Street2')
    arabic_city = fields.Char('City')
    arabic_state = fields.Char('State')
    arabic_country = fields.Char('Country')
    arabic_zip = fields.Char('Zip')
    company_national_id = fields.Char('Company National ID')
