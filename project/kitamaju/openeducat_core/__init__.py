from . import controllers
from . import models
from . import wizard

from odoo import api, SUPERUSER_ID


def _openeducat_post_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['publisher_warranty.contract'].update_notification(cron_mode=True)
