# -*- coding: utf-8 -*-
{
    'name': 'Stock Packaging Report',
    'version': '18.0.11.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Muestra cantidad de embalajes en el reporte de Existencias y en el smart button del producto',
    'description': """
        Stock Packaging Report
        ======================
        
        Este módulo añade funcionalidad para mostrar cantidades en embalajes en lugar de unidades:
        
        1. Columna "Embalajes Disponibles" en el reporte de Existencias 
           (Inventario > Reportes > Existencias)
        
        2. Smart Button del producto modificado para mostrar embalajes
           En lugar de "Disponible 5.030 U", muestra "Disponible 503 Cajas" 
           (o el nombre del embalaje configurado)
        
        Funcionamiento:
        ---------------
        1. Configure el nombre del tipo de embalaje en:
           Inventario > Configuración > Ajustes > Nombre del Embalaje para Stock
        
        2. Defina los packagings en cada producto con el nombre configurado
           (pestaña Inventario > sección Embalajes)
        
        3. El sistema calculará automáticamente:
           Stock Disponible (unidades) / Unidades por Embalaje = Cantidad de Embalajes
        
        Ejemplo:
        --------
        * Configuración: Nombre del embalaje = "Caja"
        * Producto "Azúcar" tiene packaging con name="Caja" y qty=10 (10 unidades por caja)
        * Stock disponible = 5.030 unidades
        * Smart button mostrará: "Disponible 503 Cajas" (5030 ÷ 10 = 503)
        * Columna en reporte mostrará: 503.0
        
        Características:
        ----------------
        * Smart button del producto modificado para mostrar embalajes en lugar de unidades
        * Nueva columna "Embalajes Disponibles" en Inventario > Reportes > Existencias
        * Configuración sencilla desde Ajustes de Inventario
        * Cálculo automático basado en los packagings ya definidos en Odoo
        * No requiere duplicar información: usa el qty existente en product.packaging
        * Compatible con Odoo 18 Enterprise Edition
        
        Changelog v11.0.0:
        ------------------
        * NEW: Smart button del producto ahora muestra cantidad de embalajes
        * NEW: El smart button muestra el nombre del embalaje configurado (ej: "Cajas", "Bultos")
        * FIX: Cálculo correcto en el smart button: unidades ÷ unidades_por_embalaje
        * IMPROVE: Modelo product.template extendido con campos de embalajes
        * IMPROVE: Vista del formulario del producto modificada para el nuevo smart button
    """,
    'author': 'Trixocom',
    'website': 'https://github.com/trixocom/odoo_stock_packaging_report',
    'license': 'LGPL-3',
    'depends': ['stock', 'product'],
    'data': [
        'data/system_parameters.xml',
        'views/res_config_settings_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
