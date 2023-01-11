from odoo.tests import common, TransactionCase


class TestFeesCommon(TransactionCase):
    def setUp(self):
        super(TestFeesCommon, self).setUp()
        self.op_student_fees = self.env['km.student.fees.details']
        self.op_student = self.env['km.student']
        self.op_fees_wizard = self.env['fees.detail.report.wizard']
        self.op_fees_terms = self.env['km.fees.terms']
