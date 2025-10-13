# -*- coding: utf-8 -*-
{
    'name': 'Stock Packaging Report',
    'version': '18.0.11.3.0',
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
        
        Changelog v11.3.0:
        ------------------
        * FIX CRÍTICO: Reemplazar contenido del botón existente en lugar de crear uno nuevo
        * El módulo ahora modifica directamente el smart button "Disponible" original
        * Eliminado intento de ocultar botón y crear uno nuevo (causaba que no se vieran cambios)
        * Simplificado código de herencia de vistas
        
        Changelog v11.2.0:
        ------------------
        * FIX: Actualizado a sintaxis de Odoo 18 (sin attrs, solo invisible)
        * FIX: Removido uso de attrs={'invisible': ...} reemplazado por invisible="..."
        * IMPROVE: Código compatible con Odoo 18.0+ (post v17.0)
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
