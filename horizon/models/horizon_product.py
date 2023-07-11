from odoo import api, models, fields


class ProductProduct(models.Model):
    _inherit = "product.template"

    x_retail_ratio = fields.Float(string="profit margin %")
    x_min_selling_price = fields.Float(
        string="Min Selling Price",
        compute="compute_min_selling_price",
    )

    @api.depends("x_retail_ratio", "list_price")
    def compute_min_selling_price(self):
        self.x_min_selling_price = self.standard_price + (
            (self.standard_price * self.x_retail_ratio) / 100
        )


class Employee(models.Model):
    _inherit = "hr.employee"

    x_weight = fields.Integer(string="Assigned Goals", readonly=True)
    x_total_weighted_score = fields.Integer(
        string="Total Weighted Score", readonly=True
    )
