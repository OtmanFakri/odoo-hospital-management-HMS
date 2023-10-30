from odoo import models, fields


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient Model for Hospital Management System'

    name = fields.Char(string='Nom du Patient')
    body = fields.Date(string='Date de naissance')
    phone = fields.Char(string='Téléphone')
    address = fields.Char(string='Adresse')
    gender = fields.Selection([
        ('male', 'Homme'),
        ('female', 'Femme')
    ], string='Sexe')
    blood_grp = fields.Selection([
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ], string='Blood Group')
    note = fields.Text(string='Notes')
    prescription = fields.Text(string='Prescription')
