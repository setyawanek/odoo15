from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpBatch(models.Model):
    _name = "km.batch"
    _inherit = "mail.thread"
    _description = "OpenEduCat Batch"

    code = fields.Char('Code', size=16, required=True)
    name = fields.Char('Name', size=32, required=True)
    start_date = fields.Date(
        'Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date('End Date', required=True)
    course_id = fields.Many2one('km.course', 'Course', required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_batch_code',
         'unique(code)', 'Code should be unique per batch!')]

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(
                    _("End Date cannot be set before Start Date."))

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('get_parent_batch', False):
            lst = []
            lst.append(self.env.context.get('course_id'))
            courses = self.env['km.course'].browse(lst)
            while courses.parent_id:
                lst.append(courses.parent_id.id)
                courses = courses.parent_id
            batches = self.env['km.batch'].search([('course_id', 'in', lst)])
            return batches.name_get()
        return super(OpBatch, self).name_search(
            name, args, operator=operator, limit=limit)

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Batch'),
            'template': '/openeducat_core/static/xls/op_batch.xls'
        }]
