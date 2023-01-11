from .test_core_common import TestCoreCommon


class TestCore(TestCoreCommon):

    def setUp(self):
        super(TestCore, self).setUp()

    def test_case_1_batch(self):
        batchs = self.km_batch.search([])

        for batch in batchs:
            batch.check_dates()
            batch.name_search('BOA-S1')

    def test_case_2_course(self):
        courses = self.km_course.search([])

        for course in courses:
            course.get_import_templates()

    def test_case_3_faculty(self):
        faculty = self.km_faculty.search([])

        new_faculty = self.km_faculty.create({
            'partner_id': self.env.ref('openeducat_core.km_res_partner_30').id,
            'first_name': 'binapshah',
            'last_name': 'kalol',
            'birth_date': '2009-01-01',
            'gender': 'male',
        })

        new_faculty._onchange_name()

        for rec in faculty:
            rec._check_birthdate()
            rec._onchange_name()
            rec.create_employee()
            rec.get_import_templates()

    def test_case_4_hr_employe(self):
        employs = self.hr_emp.search([])

        for employ in employs:
            employ.onchange_user()
            employ.onchange_address_id()

    def test_case_5_res_company(self):
        users = self.res_company.search([])
        record = self.env.ref('openeducat_core.km_faculty_1'),
        users.create_user(record)

    def test_case_6_student(self):
        students = self.km_student.search([])

        vals = {
            'first_name': 'nikul',
            'middle_name': 'm',
            'last_name': 'ahir',
            'birth_date': '1999-01-01',
            'gender': 'm',
            'partner_id': self.env.ref('openeducat_core.km_res_partner_14').id

        }
        new_student = self.km_student.create(vals)
        for student in students:
            student._onchange_name()
            student._check_birthdate()
            student.get_import_templates()
        new_student.create_student_user()

    def test_case_7_subject_registartion(self):
        vals = {
            'student_id': self.env.ref('openeducat_core.km_student_1').id,
            'course_id': self.env.ref('openeducat_core.km_course_2').id,
            'batch_id': self.env.ref('openeducat_core.km_batch_1').id,
        }
        registrations = self.subject_registration.create(vals)

        for registration in registrations:
            registration.action_reset_draft()
            registration.action_reject()
            registration.action_approve()
            registration.action_submitted()
            registration.get_subjects()

    def test_case_7_update(self):
        self.km_update._get_message()
        self.km_update.update_notification(cron_mode=True)

    def test_case_8_employ_wizard(self):

        vals = {'user_boolean': True}
        employe = self.employ_wizard.create(vals)
        employe.create_employee()

    def test_case_9_faculty_user_wizard(self):

        faculty_id = self.env.ref('openeducat_core.km_faculty_1')
        vals = {'faculty_ids': [(6, 0, [faculty_id.id])]}
        faculty = self.faculty_user_wizard.create(vals)
        faculty._get_faculties()
        faculty.create_faculty_user()

    def test_case_10_studnet_wizard(self):
        student_id = self.env.ref('openeducat_core.km_student_1')
        vals = {'student_ids': [(6, 0, [student_id.id])]}
        student = self.studnet_wizard.create(vals)
        student._get_students()
        student.create_user()
