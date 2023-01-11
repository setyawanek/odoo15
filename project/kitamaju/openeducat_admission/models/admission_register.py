from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class KmAdmissionRegister(models.Model):
    _name = "km.admission.register"
    _inherit = "mail.thread"
    _description = "Admission Register"
    _order = 'id DESC'

    name = fields.Char(string='Name', required=True, readonly=True,
                       states={'draft': [('readonly', False)]})
    start_date = fields.Date(
        'Start Date', required=True, readonly=True,
        default=fields.Date.today(), states={'draft': [('readonly', False)]})
    end_date = fields.Date(
        'End Date', required=True, readonly=True,
        default=(fields.Date.today() + relativedelta(days=30)),
        states={'draft': [('readonly', False)]})
    course_id = fields.Many2one(
        'km.course', 'Course', required=True, readonly=True,
        states={'draft': [('readonly', False)]}, tracking=True)
    min_count = fields.Integer(
        'Minimum No. of Admission', readonly=True,
        states={'draft': [('readonly', False)]})
    max_count = fields.Integer(
        'Maximum No. of Admission', readonly=True,
        states={'draft': [('readonly', False)]}, default=30)
    product_id = fields.Many2one(
        'product.product', 'Course Fees', required=True,
        domain=[('type', '=', 'service')], readonly=True,
        states={'draft': [('readonly', False)]}, tracking=True)
    admission_ids = fields.One2many(
        'km.admission', 'register_id', 'Admissions')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirmed'),
         ('cancel', 'Cancelled'), ('application', 'Application Gathering'),
         ('admission', 'Admission Process'), ('done', 'Done')],
        'Status', default='draft', tracking=True)
    active = fields.Boolean(default=True)

    academic_years_id = \
        fields.Many2one('km.academic.year',
                        'Academic Year', readonly=True,
                        states={'draft': [('readonly', False)]},
                        tracking=True)
    academic_term_id = fields.Many2one('km.academic.term',
                                       'Terms', readonly=True,
                                       states={'draft': [('readonly', False)]},
                                       tracking=True)
    minimum_age_criteria = fields.Integer(
        'Minimum Required Age(Years)', default=3)

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    # Departement
    department_id = fields.Many2one(comodel_name='hr.department')

    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(
                    _("End Date cannot be set before Start Date."))

    @api.constrains('min_count', 'max_count')
    def check_no_of_admission(self):
        for record in self:
            if (record.min_count < 0) or (record.max_count < 0):
                raise ValidationError(
                    _("No of Admission should be positive!"))
            if record.min_count > record.max_count:
                raise ValidationError(_(
                    "Min Admission can't be greater than Max Admission"))

    def confirm_register(self):
        self.state = 'confirm'

    def set_to_draft(self):
        self.state = 'draft'

    def cancel_register(self):
        self.state = 'cancel'

    def start_application(self):
        self.state = 'application'

    def start_admission(self):
        self.state = 'admission'

    def close_register(self):
        self.state = 'done'


class KmUsers(models.Model):
    _inherit = 'res.users'

    name = fields.Char()
