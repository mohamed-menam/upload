from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrAppraisalGoal(models.Model):
    _name = "goal.appraisal"

    name = fields.Char(string="Name", required=True)
    goal_type = fields.Selection(
        [("personal", "Personal"), ("team", "Team"), ("company", "Company")],
        string="Goal Type",
    )

    employ = fields.Many2one("hr.employee", string="Employee", required=True)

    manager = fields.Many2one("hr.employee", string="Manager", required=True)
    hr = fields.Many2one("hr.employee", string="Hr", required=True)
    deadline = fields.Datetime(string="Deadline", required=True)
    progress = fields.Integer(string="Progress %", required=True)
    description = fields.Text(string="Description")
    score = fields.Integer(string="Score %")
    weight = fields.Integer(string="Weight %")
    type_of_measurement = fields.Selection(
        [
            ("logical", "Logical"),
            ("5 points scale", "5 Points Scale"),
            ("Percentage %", "Percentage %"),
        ],
        string="Type Of Measurement",
    )

    X_progress = fields.Float(string=" ", compute="_compute_progress")

    @api.depends("X_progress", "progress")
    def _compute_progress(self):
        self.X_progress = self.progress

    x_score = fields.Float(string=" ", compute="_compute_x_score")

    @api.depends("score", "x_score")
    def _compute_x_score(self):
        self.x_score = self.score

    weighted_score = fields.Float(
        string="Weighted score", compute="_compute_weighted_score"
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirm", "Confirm"),
        ],
        default="draft",
    )

    @api.depends("weight", "score")
    def _compute_weighted_score(self):
        self.weighted_score = (self.weight / 100) * self.score

    def weight_employee(self):
        self.state = "confirm"
        if self.employ.x_weight + self.weight > 100:
            raise ValidationError(
                "Total sum of weights for this employee is above 100. Please lower the weights."
            )
        else:
            self.employ.x_weight = self.employ.x_weight + self.weight
            self.employ.x_total_weighted_score = (
                self.employ.x_total_weighted_score + self.weighted_score
            )

    def weight_unlock(self):
        self.state = "draft"
        self.employ.x_weight = self.employ.x_weight - self.weight
        self.employ.x_total_weighted_score = (
            self.employ.x_total_weighted_score - self.weighted_score
        )
