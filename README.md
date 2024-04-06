# Práctica #1 - HIS

## Integrantes del Equipo
- Emmanuel Arizabaleta Garces
- Sebastian Zapata Rodriguez
- Juan Diego Sarmiento Canchila

## Descripción General
Este proyecto es una aplicación que simula un sistema de información hospitalario (HIS), permite hacer operaciones CRUD en una base de datos no relacional. Tambien puede leer archivos .csv, .json y .txt (con formato HL7).

Se desarrolló en Python y se maneja a través de un menú interactivo en la terminal. A continuación, se detalla la estructura y los requisitos para la ejecución del proyecto.

## Estructura del Proyecto
- Una carpeta `assets`, que contien `data`  y `dataToUpload`.
- Una carpeta `src`.
- Archivos `.env` y `.env.example` (el archivo `.env` incluye el URI de MongoDB necesario para la conexión con la base de datos en Atlas).

## Requisitos de Ejecución
- Python versión 3.11 o superior.
- Paquetes `pymongo`, `json`, `csv` (estos últimos suelen venir incluidos con Python).

## Instrucciones de Ejecución
Para ejecutar el proyecto, corra el archivo `src/main.py`.

## Menú de la Aplicación
### 1. Listar todos los pacientes en la base de datos
Muestra todas las entradas almacenadas en la base de datos.

### 2. Buscar un paciente por ID
Permite la búsqueda de pacientes por ID. Si no se encuentra, se muestra "No se encontraron pacientes". De lo contrario, se muestra la información del paciente y se crea un archivo `.txt` con estructura HL7 en `assets/data`, nombrado como `patient[ID].txt`.

### 3. Guardar todos los pacientes de los archivos en 'assets/dataToUpload'
Procesa y almacena la información de los archivos `.csv`, `.json`, `.txt` en la base de datos. Notifica si el ID ya existe y confirma si se guarda exitosamente.

### 4. Actualizar la información de un paciente por ID
Permite actualizar los datos de un paciente. Solicita el ID y, si se encuentra, muestra la información actual y permite la edición de campos con opción a guardar o salir sin cambios.

### 5. Eliminar un paciente por ID
Elimina el documento asociado al ID proporcionado. Informa si el documento no existe.

### 6. Salir
Finaliza la ejecución del programa.