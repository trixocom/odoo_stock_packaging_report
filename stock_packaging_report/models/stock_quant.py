# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools import float_round


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    packaging_quantity = fields.Float(
        string='Cantidad de Embalajes',
        compute='_compute_packaging_quantity',
        digits='Product Unit of Measure',
        help='Cantidad de embalajes calculada según el tipo de embalaje configurado en el sistema.'
    )

    @api.depends('quantity', 'available_quantity', 'product_id')
    def _compute_packaging_quantity(self):
        """
        Calcula la cantidad de embalajes basándose en:
        1. La cantidad disponible del quant
        2. El nombre del tipo de embalaje configurado en el sistema
        3. El qty definido en product.packaging para ese tipo de embalaje
        """
        # Obtener el nombre del packaging configurado en el sistema
        packaging_name = self.env['ir.config_parameter'].sudo().get_param(
            'stock_packaging_report.packaging_name',
            default=''
        )
        
        for quant in self:
            quant.packaging_quantity = 0.0
            
            # Si no hay nombre de packaging configurado, no calcular
            if not packaging_name:
                continue
            
            # Si no hay producto asociado, no calcular
            if not quant.product_id:
                continue
            
            # Buscar el packaging con el nombre configurado para este producto
            packaging = self.env['product.packaging'].search([
                ('product_id', '=', quant.product_id.id),
                ('name', '=', packaging_name)
            ], limit=1)
            
            # Si no se encuentra el packaging o no tiene qty válido, no calcular
            if not packaging or packaging.qty <= 0:
                continue
            
            # Calcular cantidad de embalajes: Stock Disponible / Unidades por Embalaje
            qty_available = quant.available_quantity
            packaging_qty = packaging.qty
            
            quant.packaging_quantity = float_round(
                qty_available / packaging_qty,
                precision_rounding=0.01
            )
