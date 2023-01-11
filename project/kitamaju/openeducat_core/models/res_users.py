from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    department_ids = fields.Many2many(comodel_name='hr.department',
                                      relation='rel_department',
                                      column1='hr_id',
                                      column2='user_id')
