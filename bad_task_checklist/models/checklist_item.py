from odoo import fields, models


class ChecklistItem(models.Model):
    _name = "checklist.item"
    _description = "Checklist Item"

    name = fields.Char(required=True)
    task_id = fields.Many2one("project.task", ondelete="cascade")
    checklist_id = fields.Many2one("checklist.checklist", ondelete="cascade")
    parent_checklist = fields.Char(related="checklist_id.name")
