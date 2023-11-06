from odoo import models, fields ,api
from datetime import date


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient Model for Hospital Management System'
    _inherit='mail.thread'

    name = fields.Char(string='Nom du Patient' ,tracking=True)
    body = fields.Date(string='Date de naissance',tracking=True)

    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    phone = fields.Char(string='Téléphone',tracking=True)
    address = fields.Char(string='Adresse',tracking=True)
    gender = fields.Selection([
        ('male', 'Homme'),
        ('female', 'Femme')
    ], string='Sexe',tracking=True)

    is_child=fields.Boolean(string="Is Child" , tracking=True ,readonly=True)

    blood_grp = fields.Selection([
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ], string='Blood Group',tracking=True)
    note = fields.Text(string='Notes',tracking=True)
    prescription = fields.Text(string='Prescription',tracking=True)



    ##Function Onchange
    @api.depends('body')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.body:
                birth_date = rec.body
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                rec.age = age
            else:
                rec.age = 0

    @api.onchange('body')
    def onchange_is_child(self):
        for rec in self:
            if rec.age > 10:
                rec.is_child = False
            else:
                rec.is_child = True
    ##End Function Onchange
