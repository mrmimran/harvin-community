from odoo.tests import TransactionCase


class TestChecklistCreation(TransactionCase):
    def setUp(self):
        """Inherited method for configuration"""
        super().setUp()
        self.checklist = self.env["checklist.checklist"].create(
            {
                "name": "Bucket List",
            }
        )
        self.checklist_item_1 = self.env["checklist.item"].create(
            {
                "name": "Villa",
                "checklist_id": self.checklist.id,
            }
        )

        self.checklist_item_2 = self.env["checklist.item"].create(
            {
                "name": "Car",
                "checklist_id": self.checklist.id,
            }
        )
        self.project_task = self.env["project.task"].create(
            {"name": "Test task", "checklist_ids": [(6, 0, [self.checklist.id])]}
        )

    def test_create_checklist(self):
        """
        Added test cases to check checklist and checklist items creation.
        """
        self.assertIn(
            self.checklist_item_1,
            self.checklist.checklist_item_ids,
            "Checklist Item 1 is not associated with the main checklist.",
        )

        self.assertIn(
            self.checklist_item_2,
            self.checklist.checklist_item_ids,
            "Checklist Item 2 is not associated with the main checklist.",
        )
        self.assertEqual(
            len(self.project_task.checklist_task_item_ids),
            0,
            "Number of checklist item doesn't match.",
        )
        self.project_task._onchange_checklist_items()
        self.assertEqual(
            len(self.project_task.checklist_task_item_ids),
            2,
            "Number of checklist item doesn't match after adding checklist to task.",
        )
        task_checklist_item = self.project_task.checklist_task_item_ids[0]
        self.assertEqual(
            task_checklist_item.state, "todo", "Initial state is not To do"
        )
        self.assertEqual(
            self.project_task.checklist_progress,
            0.0,
            "The Progress is not at inital percentage",
        )
        task_checklist_item.mark_completed()
        self.assertEqual(
            task_checklist_item.state,
            "done",
            " Checklist item was not marked as Completed",
        )
        self.assertEqual(
            self.project_task.checklist_progress,
            50.0,
            "The Progress haven't got increased ",
        )

        task_checklist_item.reset_stage()
        self.assertEqual(
            task_checklist_item.state, "todo", "Checklist item was not marked as To Do"
        )
        self.project_task.checklist_task_item_ids.unlink()
        self.assertEqual(
            self.project_task.checklist_progress,
            0.0,
            "Progress is not at initial state",
        )
