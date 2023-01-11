from odoo import models, fields


class StudentPortal(models.Model):
    _inherit = 'res.partner'

    is_parent = fields.Boolean("Is a Parent")
    is_student = fields.Boolean("Is a Student")
