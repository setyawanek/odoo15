from odoo.tests import common, TransactionCase
from ..controllers import app_main
from odoo.addons.website.tools import MockRequest


class TestCoreCommon(TransactionCase):
    def setUp(self):
        super(TestCoreCommon, self).setUp()
        self.km_batch = self.env['km.batch']
        self.km_faculty = self.env['km.faculty']
        self.km_course = self.env['km.course']
        self.res_company = self.env['res.users']
        self.km_student = self.env['km.student']
        self.hr_emp = self.env['hr.employee']
        self.subject_registration = self.env['km.subject.registration']
        self.km_update = self.env['publisher_warranty.contract']
        self.employ_wizard = self.env['wizard.km.faculty.employee']
        self.faculty_user_wizard = self.env['wizard.km.faculty']
        self.studnet_wizard = self.env['wizard.km.student']
