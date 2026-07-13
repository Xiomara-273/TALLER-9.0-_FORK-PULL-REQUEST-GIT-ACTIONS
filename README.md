# Taller 9.0 - Flujo Colaborativo en GitHub con CI/CD

Este repositorio contiene la entrega práctica correspondiente al trabajo en equipo utilizando el flujo colaborativo de GitHub mediante Forks, Branches, Pull Requests y Automatización con GitHub Actions para un entorno de desarrollo en Python.

## 👥 Integrantes del Grupo
* **Estudiante 1:** Xiomara (Dueña del Repositorio Principal)
* **Estudiante 2:** [Nombre de tu compañero]

---

## 🛠️ Objetivos del Taller
* Implementar el flujo de trabajo colaborativo mediante un repositorio base y una copia bifurcada (**Fork**).
* Trabajar con **Ramas Independientes** (`feature-Xiomara` y `feature-Joel`) para aislar el desarrollo de nuevas funcionalidades.
* Realizar un historial de control de versiones con un mínimo de **3 commits significativos** por integrante.
* Aplicar el proceso de revisión de código, asignación de **Reviewers** y aprobación de **Pull Requests**.
* Configurar e integrar un pipeline de Integración Continua (CI) con **GitHub Actions** (`build.yml`) que valide automáticamente la instalación y compilación del proyecto en cada Push y Pull Request.

---

## 📂 Estructura del Proyecto
```text
mi-proyecto-git/
├── .github/
│   └── workflows/
│       └── build.yml          # Pipeline de integración continua (CI)
├── src/
│   ├── __init__.py           # Inicializador de módulo Python
│   ├── cliente.py            # Clase Cliente (Funcionalidad Estudiante 2)
│   └── producto.py           # Clase Producto (Funcionalidad Estudiante 1)
├── requirements.txt          # Dependencias simuladas del sistema
└── setup.py                  # Script de empaquetado/compilación del proyecto

🚀 Detalle del Desarrollo Colaborativo
1. Funcionalidad: Clase Producto (Estudiante 1)
Desarrollada en la rama independiente feature-Xiomara. Implementa la lógica de gestión de productos, actualización de inventarios y cálculo de montos totales por lote.

2. Funcionalidad: Clase Cliente (Estudiante 2)
Desarrollada en la rama independiente feature-[nombre]. Implementa la gestión de perfiles de usuarios y el registro histórico de transacciones comerciales.

🤖 Integración Continua (GitHub Actions)
El archivo .github/workflows/build.yml está configurado para dispararse automáticamente ante eventos de push o pull_request en la rama principal. El pipeline realiza los siguientes pasos de forma automatizada:

Copia del código de la rama en un contenedor limpio (ubuntu-latest).

Configuración del entorno de ejecución con Python 3.11.

Actualización de herramientas internas e instalación de dependencias listadas en requirements.txt.

Ejecución del build/compilación mediante setup.py install para validar la integridad del software.
