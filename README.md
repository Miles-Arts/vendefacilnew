# Vende-Fácil

Vende-Fácil es una aplicación desarrollada para facilitar la conexión entre vendedores de productos agrícolas y compradores de alimentos del campo. Su propósito principal es actuar como intermediaria digital, permitiendo la gestión eficiente de ventas, compras, productos y usuarios dentro del ecosistema agrícola.

---

## Descripción del Proyecto

Vende-Fácil maneja distintos tipos de usuarios (**clientes** y **vendedores**), así como el registro de productos con sus características específicas (tipo, tamaño, precio, disponibilidad). También permite realizar ventas y compras, y relacionarlas con los productos comercializados.

> **Nota:** Este proyecto es exclusivamente para fines de aprendizaje y corresponde a un proyecto de estudios del programa Tecnólogo en Análisis y Desarrollo de Software del SENA. No debe ser utilizado en producción ni para fines comerciales.

---

## Tecnologías Utilizadas

### Backend
- Django
- JSON
- PostgreSQL
- ENV o VENV
- Postman

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Herramientas de Desarrollo
- Git
- GitHub
- Visual Studio Code
- Copilot Pro
- Canva
- Creadores de UML

---

## Sistema Operativo
- **Windows 11**

---

## Instalación

### Instalar Django en la terminal
```bash
py -m pip install Django==5.2.1
```

### Generar el archivo `requirements.txt`
Para mantener un registro de las dependencias del proyecto, puedes generar o actualizar el archivo `requirements.txt` utilizando el siguiente comando:
```bash
pip freeze > requirements.txt
```

---

## Conexión a la Base de Datos PostgreSQL

- **Host:** localhost
- **Usuario:** postgres
- **Contraseña:** 1234
- **Base de datos:** VendeFacil
- **Puerto:** 5432

---

## Configuración de Variables de Entorno
Antes de ejecutar la aplicación, debes crear una carpeta llamada `.env` en la raíz del proyecto. Dentro de esta carpeta, crea un archivo para definir las variables de entorno necesarias para la conexión a la base de datos y la seguridad de la aplicación. Ejemplo de variables que debes agregar:

```env
SECRET_KEY=tu_clave_secreta
PGSQL_HOST=localhost
PGSQL_USER=postgres
PGSQL_PASSWORD=tu_contraseña
PGSQL_DATABASE=VendeFacil
```

---

## Solución a Errores Comunes

- Verifica las rutas en el navegador.
- Cierra y abre Visual Studio Code si los cambios no se reflejan.
- Actualiza la página web con `Ctrl + F5`.
- Reinicia el servidor local si es necesario.
- Cierra y abre una nueva terminal si el entorno virtual no funciona correctamente.

---

## Metodología de Trabajo

Este proyecto utiliza la metodología **Kanban** para la gestión y organización de tareas. Kanban permite visualizar el flujo de trabajo, identificar cuellos de botella y mejorar la eficiencia del equipo.

---

## Arquitectura del Proyecto

El proyecto utiliza una arquitectura **MVC** (Modelo-Vista-Controlador):

- **Modelo (Model):** Gestiona la lógica de datos y la conexión a la base de datos (por ejemplo, archivos como `src/conexion_postgresql.py`).
- **Vista (View):** Corresponde a la interfaz de usuario, ubicada en la carpeta `templates/` con archivos HTML.
- **Controlador (Controller):** Maneja la lógica de la aplicación y las rutas, como en `app.py`.

Esta arquitectura permite separar responsabilidades, facilitando el mantenimiento y la escalabilidad del proyecto.

---

## Versión del Proyecto

Actualmente en la versión **0.0.1** (etapa temprana de desarrollo). Se sigue el esquema de versionado semántico.

---

## Autor e Institución

- **Autor:** Milton Figueredo ([LinkedIn](#) | [GitHub](#))
- **Institución:** SENA - Servicio Nacional de Aprendizaje
- **Programa:** Tecnólogo en Análisis y Desarrollo de Software
- **Fecha:** Mayo 2025

---

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.

© 2025 Milton Figueredo