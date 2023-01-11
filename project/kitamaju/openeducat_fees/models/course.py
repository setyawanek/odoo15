from odoo import models, fields


class OpCourse(models.Model):
    _inherit = "km.course"

    fees_term_id = fields.Many2one('km.fees.terms', 'Fees Term')
