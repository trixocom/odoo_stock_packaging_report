# Stock Packaging Report

Módulo de Odoo 18 que añade una columna de "Cantidad de Embalajes" en el reporte de stock, calculada automáticamente según el tipo de embalaje configurado.

## 📋 Descripción

Este módulo permite visualizar el stock disponible en términos de embalajes (cajas, pallets, bultos, etc.) en lugar de unidades individuales, facilitando la gestión logística y de almacén.

## ✨ Características

- ✅ Nueva columna "Cantidad de Embalajes" en el reporte de stock
- ✅ Configuración sencilla desde Ajustes de Inventario
- ✅ Cálculo automático basado en los packagings ya definidos en Odoo
- ✅ No requiere duplicar información: usa el qty existente en `product.packaging`
- ✅ Compatible con Odoo 18

## 🔧 Instalación

1. Clonar o descargar este repositorio en tu carpeta de addons de Odoo:
```bash
cd /ruta/a/odoo/addons
git clone https://github.com/trixocom/odoo_stock_packaging_report.git
```

2. Actualizar la lista de aplicaciones en Odoo
3. Buscar "Stock Packaging Report" e instalar el módulo

## ⚙️ Configuración

### Paso 1: Configurar el nombre del embalaje

Ve a: **Inventario > Configuración > Ajustes**

En la sección **"Reporte de Embalajes en Stock"**, configura:
- **Nombre del Embalaje para Stock**: Especifica el nombre exacto del tipo de embalaje que deseas usar (ej: "Caja", "Pallet", "Bulto")

### Paso 2: Asegúrate que tus productos tienen packagings configurados

El módulo utiliza los packagings ya existentes en Odoo. Para cada producto, asegúrate de tener configurado al menos un packaging:

1. Ve a: **Inventario > Productos > Productos**
2. Abre un producto
3. Ve a la pestaña **"Inventario"**
4. En la sección **"Embalajes"**, agrega o edita un packaging:
   - **Nombre**: Debe coincidir exactamente con el configurado en Ajustes (ej: "Caja")
   - **Cantidad**: Define cuántas unidades contiene ese embalaje (ej: 12)

## 📊 Funcionamiento

### Ejemplo práctico:

1. **Configuración en Ajustes:**
   - Nombre del embalaje = `"Caja"`

2. **Producto "Tornillo M6":**
   - Tiene un packaging configurado:
     - Nombre: `"Caja"`
     - Cantidad: `12` (12 unidades por caja)
   - Stock disponible: `144 unidades`

3. **Resultado en el reporte de stock:**
   - Cantidad de Embalajes = `144 / 12 = 12.0 cajas`

### Fórmula de cálculo:

```
Cantidad de Embalajes = Stock Disponible ÷ Unidades por Embalaje
```

Donde:
- **Stock Disponible**: El campo `available_quantity` del `stock.quant`
- **Unidades por Embalaje**: El campo `qty` del `product.packaging` cuyo `name` coincide con el configurado

## 🎯 Casos de uso

### Gestión de almacén
Visualiza rápidamente cuántas cajas, pallets o bultos tienes de cada producto para optimizar el espacio.

### Logística y envíos
Calcula fácilmente cuántos embalajes completos puedes enviar o necesitas recibir.

### Inventario físico
Facilita el conteo físico por embalajes en lugar de unidades individuales.

## 🔍 Notas importantes

1. **Nombre exacto**: El nombre del embalaje en la configuración debe coincidir EXACTAMENTE con el nombre del packaging del producto (case-sensitive).

2. **Sin packaging configurado**: Si un producto no tiene un packaging con el nombre configurado, su "Cantidad de Embalajes" se mostrará como `0.0`.

3. **Múltiples packagings**: Si un producto tiene varios tipos de embalaje (Caja, Pallet, Bulto), el módulo solo usará el que coincida con el nombre configurado en Ajustes.

4. **Valores decimales**: Los resultados se redondean a 2 decimales, permitiendo ver embalajes parciales (ej: `12.5 cajas`).

## 🛠️ Información técnica

### Modelos modificados

- **`stock.quant`**: Añade el campo computado `packaging_quantity`
- **`res.config.settings`**: Añade el campo de configuración `packaging_name_for_stock`

### Dependencias

- `stock`: Módulo de inventario de Odoo
- `product`: Módulo de productos de Odoo

### Parámetros del sistema

El módulo utiliza el siguiente parámetro de sistema:
- `stock_packaging_report.packaging_name`: Almacena el nombre del packaging configurado (default: "Caja")

## 📝 Changelog

### Version 2.0.0 (2025-10-11)
- ✨ Refactorización completa del cálculo
- ✨ Ahora usa el campo `qty` existente de `product.packaging`
- ✨ Configuración por nombre de packaging en lugar de cantidad fija
- ✨ Interfaz de configuración mejorada en Ajustes de Inventario
- ✨ Documentación extendida con ejemplos

### Version 1.0.0
- 🎉 Versión inicial

## 📄 Licencia

LGPL-3

## 👤 Autor

**Trixocom**
- GitHub: [@trixocom](https://github.com/trixocom)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🐛 Reporte de bugs

Si encuentras algún error, por favor abre un issue en: https://github.com/trixocom/odoo_stock_packaging_report/issues

## ❓ Soporte

Para preguntas o soporte, abre un issue en el repositorio de GitHub.
