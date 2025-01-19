from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    checklist_progress = fields.Float(store=True, compute="_compute_checklist_progress")
    checklist_ids = fields.Many2many(
        comodel_name="checklist.checklist",
        string="Checklists",
    )

    checklist_task_item_ids = fields.One2many(
        comodel_name="task.checklist.item",
        inverse_name="task_id",
        string="Task Checklist Items",
        store=True,
    )

    @api.onchange("checklist_ids")
    def _onchange_checklist_items(self):
        """Automatically adds checklist items to tasks when the checklist is updated."""
        for task in self:
            existing_items = task.checklist_task_item_ids.mapped("item_id").ids
            checklist_task_item_ids = [
                (
                    0,
                    0,
                    {
                        "name": item.name,
                        "state": "todo",
                        "checklist_id": item.checklist_id.id,
                        "item_id": item.id,
                    },
                )
                for item in task.mapped("checklist_ids.checklist_item_ids")
                if item._origin.id not in existing_items
            ]
            task.update({"checklist_task_item_ids": checklist_task_item_ids})

    @api.depends("checklist_task_item_ids.state", "checklist_task_item_ids")
    def _compute_checklist_progress(self):
        """Calculate checklist progress"""
        for task in self:
            total_items = len(task.checklist_task_item_ids)
            if total_items > 0:
                completed_items = task.checklist_task_item_ids.filtered(
                    lambda item: item.state == "done"
                )
                progress = (len(completed_items) / total_items) * 100
                task.checklist_progress = progress
            else:
                task.checklist_progress = 0.0
