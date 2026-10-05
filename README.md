# Restaurante App 
## Tema
Manejo de eventos con Tkinter

## Datos del estudiante

**Nombre**: Bonner Javier García Guanga

## Descripción del proyecto
restaurante_app es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO) y la biblioteca Tkinter para la gestión básica de un restaurante. El sistema permite administrar usuarios, productos y ventas mediante una interfaz gráfica organizada y una arquitectura modular.

Esta versión corresponde a la evolución realizada en la Semana 16, donde se incorporó el manejo de eventos mediante bind(), manteniendo todas las funcionalidades implementadas en semanas anteriores.

## Objetivo de la semana 16

- Aplicar eventos y callbacks en una interfaz gráfica.
- Utilizar bind() para responder a interacciones del usuario.
- Implementar gestión de usuarios mediante formularios y tablas.
- Mantener la separación entre interfaz, lógica de negocio y persistencia.
- Reutilizar métodos existentes evitando duplicación de código.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/                  
├── main.py
└── README.md
```

## Capas

`modelos/`: define las clases `Usuario` y `Producto` y `Venta`, con validaciones basicas para evitar campos vacios.

`servicios/`: contiene la logica de consulta, registro, actualizacion, eliminacion y persistencia. `RestauranteServicio` tambien registra ventas.

`datos/`: guarda la informacion persistente en archivos JSON.

`ui/`: contiene las vistas creadas con Tkinter.

`assets/icons/`: contiene los iconos PNG usados por los botones. 

`assets/logo/`: contiene la identidad visual principal de la aplicacion. `logo.png` se muestra dentro de la interfaz y `icono.png` se usa como icono de la ventana.

## Pantallas principales

`LoginView`: pantalla de inicio de sesion.

`Inicio`: panel de resumen con usuarios, libros y ventas.

`Usuarios`: pantalla de consulta de usuarios registrados.

`Productos`: pantalla de gestion con formulario, botones y tabla para el CRUD basico.

`Ventas`: pantalla nueva para seleccionar un usuario, seleccionar un producto y registrar una venta simple.

## Componentes Tkinter utilizados

`Label`: textos y titulos.

`Entry`: campos de entrada para login y formulario de productos.

`ttk.Combobox`: selectores de usuario y producto en la vista de ventas.

`ttk.Button`: botones de navegacion y acciones con `command=`.

`ttk.Treeview`: tablas de usuarios, productos y ventas.

`ttk.Scrollbar`: barra de desplazamiento para las tablas.

`messagebox`: mensajes simples de confirmacion o error.

## Nueva funcionalidad

**Gestión de usuarios**

- Registrar usuarios.
- Consultar usuarios.
- Actualizar usuarios.
- Eliminar usuarios.
- Persistencia en usuarios.json.
- Visualización mediante Treeview.

**Roles de usuario**

El sistema incorpora tres roles básicos:

- Administrador
- Empleado
- Cliente

El usuario Administrador tiene acceso a la gestión de usuarios. Los usuarios Empleado y Cliente no disponen de permisos administrativos.

## Eventos implementados

**Evento Treeview**

Se utiliza el evento:
```text
<<TreeviewSelect>>
```
Cuando el usuario selecciona una fila de la tabla:

1. Se obtiene el identificador del registro.
2. Se consulta el usuario mediante RestauranteServicio.
3. Se cargan automáticamente los datos en el formulario.

Flujo:
```text
Treeview
   ↓
<<TreeviewSelect>>
   ↓
bind()
   ↓
callback(event)
   ↓
RestauranteServicio
   ↓
Formulario
```
---

**Evento Enter**

Se utiliza:
```text
<Return>
```
Permite registrar un usuario presionando la tecla Enter.

El callback reutiliza el método de registro existente para evitar duplicación de lógica.

---

**Evento Escape**

Se utiliza:
```text
<Escape>
```
Permite:

- Limpiar el formulario.
- Cancelar la selección actual.
- Restablecer el estado inicial de la interfaz.

---

**Evento Combobox**

Se utiliza:
```text
<<ComboboxSelected>>
```
Permite responder al cambio del rol seleccionado en el formulario de usuarios.

---

**Botones mediante command=**

Las acciones principales continúan utilizando command=:

- Registrar
- Actualizar
- Eliminar
- Limpiar

Esto permite diferenciar claramente el uso de command= y bind().

## Persistencia

La información se almacena mediante archivos JSON:

- usuarios.json
- productos.json
- ventas.json

La interfaz gráfica no accede directamente a los archivos. Todas las operaciones son gestionadas por RestauranteServicio y ArchivoServicio.


## Control de acceso

La aplicacion usa el objeto `usuario_actual` recibido por `MainView`.

Regla sencilla:

- `Administrador`: puede ver y usar la seccion `Usuarios`.
- `Empleado` y `Cliente`: no ven la opcion `Usuarios` en el menu lateral.


## Ejecución del proyecto

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:
```text
python main.py
```
3. Iniciar sesión con un usuario registrado.
4. Acceder a las opciones disponibles según el rol del usuario.

## Credencial de demostración

Usuario: `admin`

Contrasena: `1234`

Tambien puede usarse:

Usuario: `maria`

Contrasena: `abcd`

Usuario cliente de prueba:

Usuario: `joel`

Contrasena: `cliente123`

## Conclusión
La Semana 16 permitió incorporar eventos y callbacks en la aplicación restaurante_app, fortaleciendo la interacción entre el usuario y la interfaz gráfica. Se mantuvo la arquitectura modular desarrollada en semanas anteriores y se integraron mecanismos como Treeview, Combobox y eventos de teclado, garantizando una aplicación organizada, reutilizable y fácil de mantener.