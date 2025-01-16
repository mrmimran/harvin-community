from odoo import models, fields


class ProjectCategory(models.Model):
    _name = 'project.category'

    name = fields.Char(string="Category")
    color = fields.Integer(string="Color")
