from odoo.tests import common, TransactionCase


class TestAdmissionCommon(TransactionCase):
    def setUp(self):
        super(TestAdmissionCommon, self).setUp()
        self.op_register = self.env['km.admission.register']
        self.op_admission = self.env['km.admission']
        self.wizard_admission = self.env['admission.analysis']
