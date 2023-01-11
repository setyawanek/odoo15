from odoo import models, api, fields, exceptions, _


class OpFeesTermsLine(models.Model):
    _name = "km.fees.terms.line"
    _rec_name = "due_days"
    _description = "Fees Details Line"

    due_days = fields.Integer('Due Days')
    due_date = fields.Date('Due Date')
    value = fields.Float('Value (%)')
    fees_element_line = fields.One2many("km.fees.element",
                                        "fees_terms_line_id", "Fees Elements")
    fees_id = fields.Many2one('km.fees.terms', 'Fees')


class OpFeesTerms(models.Model):
    _name = "km.fees.terms"
    _inherit = "mail.thread"
    _description = "Fees Terms For Course"

    name = fields.Char('Fees Terms', required=True)
    active = fields.Boolean('Active', default=True)
    fees_terms = fields.Selection([('fixed_days', 'Fixed Fees of Days'),
                                   ('fixed_date', 'Fixed Fees of Dates')],
                                  string='Term Type', default='fixed_days')
    note = fields.Text('Description')
    company_id = fields.Many2one('res.company', 'Company', required=True,
                                 default=lambda s: s.env.user.company_id)
    no_days = fields.Integer('No of Days')
    day_type = fields.Selection([('before', 'Before'), ('after', 'After')],
                                'Type')
    line_ids = fields.One2many('km.fees.terms.line', 'fees_id', 'Terms')
    discount = fields.Float(string='Discount (%)',
                            digits='Discount', default=0.0)

    @api.model
    def create(self, vals):
        res = super(OpFeesTerms, self).create(vals)
        if not res.line_ids:
            raise exceptions.AccessError(_("Fees Terms must be Required!"))
        total = 0.0
        for line in res.line_ids:
            if line.value:
                total += line.value
        if total != 100.0:
            raise exceptions.AccessError(
                _("Fees terms must be divided as such sum up in 100%"))
        return res


class OpStudentCourseInherit(models.Model):
    _inherit = "km.student.course"

    fees_term_id = fields.Many2one('km.fees.terms', 'Fees Term')
    fees_start_date = fields.Date('Fees Start Date')
