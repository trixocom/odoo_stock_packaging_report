# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools import float_round


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    packaging_quantity = fields.Float(
        string='Cantidad de Embalajes',
        compute='_compute_packaging_quantity',
        digits='Product Unit of Measure',
        help='Cantidad de embalajes calculada según el parámetro del sistema.'
    )

    @api.depends('quantity', 'available_quantity')
    def _compute_packaging_quantity(self):
        """
        Calcula la cantidad de embalajes basándose en la cantidad disponible
        y el tamaño de embalaje definido en los parámetros del sistema.
        """
        # Obtener el parámetro del sistema para el tamaño del embalaje
        packaging_size = float(
            self.env['ir.config_parameter'].sudo().get_param(
                'stock_packaging_report.packaging_size', 
                default='1.0'
            )
        )
        
        # Validar que el tamaño del embalaje sea válido
        if packaging_size <= 0:
            packaging_size = 1.0
        
        for quant in self:
            # Usar available_quantity (disponible) en lugar de quantity total
            # para mostrar solo lo que realmente está disponible para usar
            qty = quant.available_quantity
            
            # Calcular cantidad de embalajes
            if packaging_size > 0:
                quant.packaging_quantity = float_round(
                    qty / packaging_size,
                    precision_rounding=0.01
                )
            else:
                quant.packaging_quantity = 0.0
