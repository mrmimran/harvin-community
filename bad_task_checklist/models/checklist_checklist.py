from odoo import fields, models


class ChecklistChecklist(models.Model):
    _name = "checklist.checklist"
    _description = "Checklist"

    name = fields.Char(string="Checklist Name", required=True)
    checklist_item_ids = fields.One2many(
        "checklist.item", "checklist_id", string="CheckList Items", required=True
    )
