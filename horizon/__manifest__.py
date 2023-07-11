# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "horizon",
    "version": "1.1",
    "summary": "MY First Model",
    "author": "QuadroZona",
    "sequence": 1,
    "description": """DarBelal""",
    "category": "Invoicing Management",
    "website": "https://www.odoo.com/page/billing",
    "license": "LGPL-3",
    "depends": [
        "sale_management",
        "account",
        "l10n_generic_coa",
        "hr",
        "sale_discount_total",
        "crm",
    ],
    "data": ["security/ir.model.access.csv", "views/productedite.xml"],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
