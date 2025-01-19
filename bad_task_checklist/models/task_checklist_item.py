from odoo import fields, models


class TaskChecklistItem(models.Model):
    _name = "task.checklist.item"
    _description = "Task Checklist Item"

    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        required=True,
        ondelete="cascade",
    )
    checklist_id = fields.Many2one("checklist.checklist", ondelete="cascade")
    name = fields.Char(string="Item", required=True)
    state = fields.Selection(
        string="Status",
        required=True,
        readonly=True,
        copy=False,
        selection=[
            ("todo", "To Do"),
            ("done", "Done"),
        ],
        default="todo",
    )

    completed_date = fields.Date()
    item_id = fields.Many2one("checklist.item", string="Task Item Id")

    def mark_completed(self):
        """Change state field to done"""
        self.write({"state": "done", "completed_date": fields.Date.today()})

    def reset_stage(self):
        """Change state field to todo"""
        self.write({"state": "todo", "completed_date": False})
