# 📦 Stock Packaging Report - Módulo Odoo 18

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-purple.svg)](https://www.odoo.com)
[![Version](https://img.shields.io/badge/version-11.0.0-green.svg)](https://github.com/trixocom/odoo_stock_packaging_report)

## 📋 Descripción

Módulo para Odoo 18 que **transforma la visualización del stock** de unidades a **embalajes** (cajas, bultos, pallets, etc.) en:

1. **Smart Button del producto**: Reemplaza "Disponible X U" por "Disponible X Cajas"
2. **Reporte de Existencias**: Agrega columna "Embalajes Disponibles"

### 🎯 Problema que resuelve

**Antes del módulo:**
- Smart button muestra: "Disponible 5.030 U" ❌
- Difícil calcular cuántos embalajes hay en stock

**Con el módulo:**
- Smart button muestra: "Disponible 503 Cajas" ✅
- Cálculo automático: 5.030 unidades ÷ 10 unidades/caja = 503 cajas

---

## ✨ Características Principales

### 1. Smart Button Modificado
- **Ubicación**: Formulario del producto (botón superior derecho)
- **Antes**: `Disponible 5.030 U`
- **Ahora**: `Disponible 503 Cajas` (o el nombre configurado)
- **Cálculo**: Stock Disponible ÷ Unidades por Embalaje

### 2. Columna en Reporte de Existencias
- **Ubicación**: Inventario > Reportes > Existencias
- **Columna**: "Embalajes Disponibles"
- **Muestra**: Cantidad calculada de embalajes por producto

---

## 🚀 Instalación

### Requisitos previos
- Odoo 18 Enterprise Edition
- Módulos: `stock`, `product`

### Pasos de instalación

1. **Clonar el repositorio:**
```bash
cd /mnt/extra-addons
git clone https://github.com/trixocom/odoo_stock_packaging_report.git
```

2. **Reiniciar Odoo:**
```bash
sudo systemctl restart odoo
```

3. **Activar modo desarrollador:**
   - Ajustes > Activar el modo de desarrollador

4. **Actualizar lista de aplicaciones:**
   - Aplicaciones > Actualizar lista de aplicaciones

5. **Instalar el módulo:**
   - Buscar "Stock Packaging Report"
   - Clic en **Instalar**

---

## ⚙️ Configuración

### Paso 1: Configurar el nombre del embalaje

1. Ir a **Inventario > Configuración > Ajustes**
2. Buscar la sección **"Nombre del Embalaje para Stock"**
3. Ingresar el nombre exacto del tipo de embalaje (ejemplo: `"Caja"`, `"Bulto"`, `"Pallet"`)
4. Clic en **Guardar**

![Configuración](https://via.placeholder.com/800x200/4CAF50/FFFFFF?text=Inventario+>+Configuración+>+Ajustes)

### Paso 2: Configurar packagings en los productos

Para cada producto que quieras mostrar en embalajes:

1. Abrir el producto
2. Ir a la pestaña **"Inventario"**
3. En la sección **"Embalajes"**, agregar o editar un packaging:
   - **Nombre**: Debe coincidir **exactamente** con el configurado en Ajustes (ej: `"Caja"`)
   - **Cantidad**: Define cuántas unidades contiene ese embalaje (ej: `10`)

![Packaging del Producto](https://via.placeholder.com/800x300/2196F3/FFFFFF?text=Producto+>+Inventario+>+Embalajes)

---

## 📊 Ejemplo de Uso

### Configuración del sistema:
- **Nombre del embalaje configurado**: `"Caja"`

### Producto: "Azúcar Ledesma X 1 KG"
- **Packaging configurado**:
  - Nombre: `"Caja"`
  - Cantidad: `10` unidades por caja
- **Stock disponible**: `5.030 unidades`

### Resultados:

#### Smart Button del producto:
```
┌─────────────────┐
│   📦 Disponible │
│      503        │
│     Cajas       │
└─────────────────┘
```

#### Columna en Reporte de Existencias:
| Producto | Cantidad Disponible | **Embalajes Disponibles** |
|----------|---------------------|---------------------------|
| Azúcar Ledesma X 1 KG | 5.030 U | **503.0 Cajas** |

### Fórmula de cálculo:
```
Embalajes = Stock Disponible ÷ Unidades por Embalaje
          = 5.030 ÷ 10
          = 503 cajas
```

---

## 🎯 Casos de Uso

### 📦 Gestión de almacén
Visualiza rápidamente cuántas cajas, pallets o bultos tienes para optimizar el espacio.

### 🚚 Logística y envíos
Calcula fácilmente cuántos embalajes completos puedes enviar o necesitas recibir.

### 📝 Inventario físico
Facilita el conteo físico por embalajes en lugar de unidades individuales.

### 💼 Planificación de compras
Determina cuántos embalajes necesitas comprar basándote en el stock actual.

---

## 🔧 Funcionamiento Técnico

### Modelos extendidos

#### `product.template`
- **Campo nuevo**: `packaging_quantity_available` (Float computado)
  - Calcula: `qty_available / packaging.qty`
- **Campo nuevo**: `packaging_name_display` (Char computado)
  - Obtiene el nombre del embalaje configurado

#### `product.product`
- **Campo nuevo**: `packaging_quantity_available` (Float computado)
  - Mismo cálculo que en product.template

### Vistas modificadas

#### `product_template_form_view`
- **Smart button modificado**: Muestra embalajes en lugar de unidades
- **XPath**: Reemplaza el botón `action_open_quants`

#### `product_product_stock_tree`
- **Nueva columna**: "Embalajes Disponibles"
- **Posición**: Después de "Cantidad Disponible"

### Parámetros del sistema

- **Clave**: `stock_packaging_report.packaging_name`
- **Valor**: Nombre del packaging configurado (default: vacío)
- **Ubicación**: Configuración de Inventario

---

## ⚠️ Notas Importantes

### ✅ Nombre exacto
El nombre del embalaje en la configuración debe coincidir **EXACTAMENTE** con el nombre del packaging del producto (es case-sensitive).

**Ejemplo:**
- ❌ Configuración: `"caja"` | Producto: `"Caja"` → No funcionará
- ✅ Configuración: `"Caja"` | Producto: `"Caja"` → Funcionará

### ⚠️ Sin packaging configurado
Si un producto no tiene un packaging con el nombre configurado:
- Smart button mostrará la cantidad de unidades (`qty_available`)
- Columna "Embalajes Disponibles" mostrará `0.0`

### 📦 Múltiples packagings
Si un producto tiene varios tipos de embalaje (Caja, Pallet, Bulto), el módulo solo usará el que coincida con el nombre configurado en Ajustes.

### 🔢 Valores decimales
Los resultados se redondean a 2 decimales, permitiendo ver embalajes parciales (ej: `12.5 cajas`).

---

## 🐛 Solución de Problemas

### El smart button sigue mostrando unidades (U)

**Causa**: El producto no tiene un packaging configurado con el nombre exacto.

**Solución**:
1. Verificar que el nombre del embalaje en Ajustes sea exacto
2. Ir al producto > pestaña Inventario > Embalajes
3. Crear/editar un packaging con el nombre exacto
4. Refrescar la página (Ctrl + Shift + R)

### La columna no aparece en el reporte

**Solución**:
1. Ir a Inventario > Reportes > Existencias
2. Clic en el icono de columnas (☰)
3. Activar "Embalajes Disponibles"
4. Refrescar con Ctrl + Shift + R

### El cálculo es incorrecto

**Verificar**:
1. El campo `qty` del packaging está correctamente configurado
2. El `qty_available` del producto es correcto
3. Refrescar el navegador y volver a calcular

---

## 📝 Changelog

### Version 11.0.0 (2025-10-13)
- ✨ **NEW**: Smart button del producto modificado para mostrar embalajes
- ✨ **NEW**: Nombre del embalaje visible en el smart button
- 🔧 **FIX**: Cálculo correcto: unidades ÷ unidades_por_embalaje
- 🎯 **IMPROVE**: Modelo product.template extendido
- 🎨 **IMPROVE**: Vista del formulario del producto mejorada

### Version 10.0.0 (2025-10-12)
- 🔧 **FIX**: Herencia correcta de vista de reporte de existencias
- 📚 **DOCS**: Documentación completa agregada

### Version 2.0.0 (2025-10-11)
- ✨ Refactorización completa del cálculo
- ✨ Uso del campo `qty` existente de `product.packaging`
- ✨ Configuración por nombre de packaging

---

## 📄 Licencia

LGPL-3

---

## 👤 Autor

**Trixocom**
- GitHub: [@trixocom](https://github.com/trixocom)
- Web: [https://trixocom.com](https://trixocom.com)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas! 

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📞 Soporte

Si encuentras algún problema o tienes alguna pregunta:

- 🐛 Reporta bugs en [GitHub Issues](https://github.com/trixocom/odoo_stock_packaging_report/issues)
- 💬 Preguntas en [GitHub Discussions](https://github.com/trixocom/odoo_stock_packaging_report/discussions)

---

## ⭐ ¿Te gusta este módulo?

Si este módulo te resulta útil, ¡no olvides darle una ⭐ en GitHub!

---

**Última actualización**: Octubre 2025
