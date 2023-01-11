from odoo import models, api


class ReportFeesAnalysis(models.AbstractModel):
    _name = "report.openeducat_fees.report_fees_analysis"
    _description = "Fees Report"

    def get_invoice_amount(self, student_id):
        total_amount = 0.0
        paid_amount = 0.0
        inv_res = 0.0
        account_move_id = self.env['account.move'].search([
            ('partner_id', '=', student_id.partner_id.id),
            ('state', 'in', ['posted'])])
        for inv in account_move_id:
            if inv.payment_reference:
                for inv_line_id in inv.invoice_line_ids:
                    total_amount += inv_line_id.price_unit
                inv_res += inv.amount_residual
        paid_amount = total_amount - inv_res
        return [total_amount, paid_amount]

    @api.model
    def _get_report_values(self, docids, data=None):
        student_ids = []
        if data['fees_filter'] == 'student':
            student_ids = self.env['km.student'].browse([data['student']])
        else:
            student_ids = self.env['km.student'].search(
                [('course_detail_ids.course_id', '=', data['course'])])
        docargs = {
            'doc_ids': self.ids,
            'doc_model': 'km.student',
            'docs': student_ids,
            'get_invoice_amount': self.get_invoice_amount,
        }
        return docargs
