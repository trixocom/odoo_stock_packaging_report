# Stock Packaging Report

## Descripción

Este módulo para Odoo 18 Enterprise Edition añade una columna en el reporte de stock que muestra la **cantidad de embalajes** en lugar de solo mostrar la cantidad de unidades.

El tamaño del embalaje es completamente parametrizable desde los parámetros del sistema, lo que permite una configuración flexible según las necesidades de cada empresa.

## Características

- ✅ Nueva columna "Cantidad de Embalajes" en el reporte de stock (Inventario > Reportes > Stock)
- ✅ Cálculo automático basado en la cantidad disponible
- ✅ Parámetro de sistema configurable para definir el tamaño del embalaje
- ✅ Compatible con Odoo 18 Enterprise Edition
- ✅ Hereda correctamente de las vistas existentes sin modificar el código base

## Instalación

1. Clone o descargue este repositorio en su carpeta de addons de Odoo:
```bash
cd /path/to/odoo/addons
git clone https://github.com/trixocom/odoo_stock_packaging_report.git stock_packaging_report
```

2. Reinicie el servidor de Odoo

3. Actualice la lista de aplicaciones:
   - Vaya a **Apps** en Odoo
   - Haga clic en el menú de tres puntos
   - Seleccione **Update Apps List**

4. Busque "Stock Packaging Report" e instálelo

## Configuración

### Configurar el tamaño del embalaje

Para configurar el tamaño del embalaje:

1. Active el modo de desarrollador:
   - Vaya a **Configuración** > **Activar el modo de desarrollador**

2. Navegue a:
   - **Configuración** > **Técnico** > **Parámetros** > **Parámetros del Sistema**

3. Busque el parámetro con la clave:
   ```
   stock_packaging_report.packaging_size
   ```

4. Modifique el valor según su necesidad. Por ejemplo:
   - `12.0` para embalajes de 12 unidades
   - `24.0` para embalajes de 24 unidades
   - `1.0` (valor por defecto) para mantener la relación 1:1

### Ejemplo de uso

Si tiene:
- 120 unidades disponibles en stock
- Tamaño de embalaje configurado en 12

La columna "Cantidad de Embalajes" mostrará: **10.00**

## Estructura del Módulo

```
stock_packaging_report/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── stock_quant.py
├── views/
│   └── stock_quant_views.xml
├── data/
│   └── system_parameters.xml
└── README.md
```

## Detalles Técnicos

### Modelo extendido: `stock.quant`

El módulo extiende el modelo `stock.quant` añadiendo un campo calculado:

```python
packaging_quantity = fields.Float(
    string='Cantidad de Embalajes',
    compute='_compute_packaging_quantity',
    digits='Product Unit of Measure',
    help='Cantidad de embalajes calculada según el parámetro del sistema.'
)
```

### Cálculo

El campo se calcula mediante:
```python
packaging_quantity = available_quantity / packaging_size
```

Donde:
- `available_quantity`: Cantidad disponible en stock (no reservada)
- `packaging_size`: Valor del parámetro del sistema

## Compatibilidad

- **Odoo Version**: 18.0 Enterprise Edition
- **Módulos requeridos**: `stock`
- **Python**: 3.10+

## Soporte

Para reportar problemas o solicitar nuevas características, por favor abra un issue en:
https://github.com/trixocom/odoo_stock_packaging_report/issues

## Licencia

Este módulo está licenciado bajo LGPL-3.

## Autor

**Trixocom**
- GitHub: [@trixocom](https://github.com/trixocom)
- Email: hectorquiroz@trixocom.com

## Notas de Versión

### Version 18.0.1.0.0
- Versión inicial
- Campo calculado `packaging_quantity`
- Parámetro de sistema configurable
- Vistas extendidas para mostrar la columna en el reporte de stock
