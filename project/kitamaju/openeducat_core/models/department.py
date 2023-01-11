from odoo import models, fields, api


class OpDepartment(models.Model):
    _name = "km.department"
    _description = "OpenEduCat Department"

    name = fields.Char('Name')
    code = fields.Char('Code')
    parent_id = fields.Many2one('km.department', 'Parent Department')

    @api.model
    def create(self, vals):
        department = super(OpDepartment, self).create(vals)
        self.env.user.write({'department_ids': [(4, department.id)]})
        return department
