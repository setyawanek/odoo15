from odoo import models, api, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.onchange('user_id')
    def onchange_user(self):
        if self.user_id:
            self.work_email = self.user_id.email
            self.identification_id = False

    @api.onchange('address_id')
    def onchange_address_id(self):
        if self.address_id:
            self.work_phone = self.address_id.phone
            self.mobile_phone = self.address_id.mobile


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    user_ids = fields.Many2many(comodel_name='res.users',
                                relation='rel_department',
                                column1='user_id',
                                column2='hr_id')
