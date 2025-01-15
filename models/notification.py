from odoo import models, fields, api

class Notification(models.Model):
    _name = 'managealvaro.notification'
    _description = 'Notification for Project Tasks and Sprints'
    _inherit = ['mail.thread']
    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    notification_date = fields.Datetime(string='Fecha de Notificación', required=True)
    user_id = fields.Many2one(
        'res.users',
        string='Usuario Asignado',
        required=True,
        default=lambda self: self.env.user
    )
    task_id = fields.Many2one('managealvaro.task', string='Tarea Relacionada')
    sprint_id = fields.Many2one('managealvaro.sprint', string='Sprint Relacionado')
    sent = fields.Boolean(string='Enviada', default=False)

    @api.model
    def create(self, vals):
        if 'user_id' not in vals:
            vals['user_id'] = self.env.user.id
        notification = super(Notification, self).create(vals)
        notification_message = f"Notificación: {notification.name} - {notification.description}"
        
        notification.message_post(
            body=notification_message,
            subject=notification.name,
            partner_ids=[notification.user_id.partner_id.id],
            type='notification'
        )
        return notification

        @api.model
        def send_notifications(self):
            notifications = self.search([('sent', '=', False), ('notification_date', '<=', fields.Datetime.now())])
            for notification in notifications:
                if notification.task_id.exists():
                    mail_template = self.env.ref('managealvaro.notification_email_template')
                    mail_template.send_mail(notification.id, force_send=True)
                    notification.sent = True
                else:
                    _logger.warning(f'Tarea {notification.task_id.id} no existe.')


