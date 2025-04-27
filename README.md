# 📝 Task Manager (Administrador de Tareas)

Bienvenido a **Task Manager**, un sistema simple para gestionar tareas desde la consola.  
Este proyecto te permite crear, listar, completar y eliminar tareas fácilmente a través de una interfaz interactiva en terminal.

---

## 🚀 Funcionalidades

- ✅ **Crear tareas**  
- 📋 **Listar todas las tareas**  
- ✔️ **Marcar tareas como completadas**  
- 🗑️ **Eliminar tareas**  
- 🖥️ **Interfaz de usuario por consola** (UI)

---

## 📂 Estructura del Proyecto

```bash
task-manager/
│
├── app.py          # Archivo principal del proyecto (menu e interacción)
├── func/           # Carpeta de funcionalidades (crear, mostrar, eliminar, completar tareas)
│   ├── create_task.py
│   ├── show_task.py
│   ├── complete_task.py
│   └── delete_task.py
│
├── save/
│   └── tasks.py    # Archivo donde se guarda la lista de tareas
│
└── README.md       # Documentación del proyecto
```

---

## 🛠️ ¿Cómo clonar y probar el proyecto?

1. **Clona el repositorio:**

```bash
git clone https://github.com/juanreina19/task-manager.git
```

2. **Entra a la carpeta del proyecto:**

```bash
cd task-manager
```

3. **Ejecuta el archivo principal `app.py`:**

```bash
python app.py
```

*(Asegúrate de tener Python instalado en tu computadora.)*

---

## 🎯 Uso del sistema

Una vez que ejecutes `app.py`, se desplegará un **menú interactivo** en la consola, donde podrás:

- Crear nuevas tareas ingresando una descripción.
- Ver todas las tareas creadas, incluyendo su estado (completado o pendiente).
- Marcar tareas como completadas.
- Eliminar tareas si ya no las necesitas.

---

## 📋 Requisitos

- Python 3.8 o superior.
