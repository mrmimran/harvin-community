from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    project_category_ids = fields.Many2many(comodel_name="project.category", string="Project Category")
