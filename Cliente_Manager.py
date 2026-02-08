# ================================
# SKY v2.0 - Gestión de Clientes
# Lenguaje: Python
# ================================

# Importamos librerías estándar de Python
import os                      
from datetime import datetime  


# --------------------------------
# Definición de rutas base
# --------------------------------

# Obtiene la ruta absoluta donde se encuentra este archivo (app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define la ruta donde se guardarán los archivos de los clientes
CLIENTS_DIR = os.path.join(BASE_DIR, "data", "clientes")


# --------------------------------
# Función: crear estructura de almacenamiento
# Crea la carpeta data/clientes si no existe
# Esto asegura que la aplicación siempre tenga un lugar donde guardar los archivos
# --------------------------------
def ensure_storage():   
    os.makedirs(CLIENTS_DIR, exist_ok=True)


# --------------------------------
# Función: obtener fecha y hora actual
# Devuelve la fecha y hora actual en formato legible para registrar cuándo se crean o modifican datos
# --------------------------------
def now_str() -> str:    
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# --------------------------------
# Función: limpiar nombre del cliente
# Convierte el nombre del cliente en un formato seguro para usar como nombre de archivo
# --------------------------------
def to_safe_filename(name: str) -> str:    
    # Elimina espacios repetidos
    name = " ".join(name.strip().split())

    # Reemplaza espacios por guión bajo
    safe = name.replace(" ", "_")

    # Conserva solo letras, números y guión bajo
    safe = "".join(ch for ch in safe if ch.isalnum() or ch == "_")

    return safe


# --------------------------------
# Función: obtener ruta del archivo del cliente
# Devuelve la ruta completa del archivo del cliente a partir de su nombre
# --------------------------------
def client_path(display_name: str) -> str:    
    safe = to_safe_filename(display_name)
    return os.path.join(CLIENTS_DIR, f"{safe}.txt")


# --------------------------------
# Función: crear cliente nuevo
# Crea un nuevo archivo para un cliente que no existe previamente
# --------------------------------
def create_new_client():    
    name = input("Nombre del cliente (persona/negocio): ").strip()

    if not name:
        print("Nombre invalido.")
        return

    path = client_path(name)

    # Verifica si el cliente ya existe
    if os.path.exists(path):
        print("El cliente ya existe.")
        return

    contact = input("Contacto (telefono/correo opcional): ").strip()
    service = input("Servicio solicitado (telefonia/internet/tv de paga): ").strip()
    desc = input("Descripción del servicio: ").strip()

    # Crea el archivo del cliente
    with open(path, "w", encoding="utf-8") as f:
        f.write("SKY - EXPEDIENTE DE CLIENTE\n")
        f.write(f"Cliente: {name}\n")
        f.write(f"Archivo: {os.path.basename(path)}\n")
        f.write(f"Contacto: {contact if contact else 'N/A'}\n")
        f.write(f"Fecha de creacion: {now_str()}\n")
        f.write("----------------------------------------\n")
        f.write("HISTORIAL DE SERVICIOS:\n")
        f.write(f"- [{now_str()}] {service} | {desc}\n")

    print("Cliente creado correctamente.")


# --------------------------------
# Función: agregar servicio a cliente existente
# Agrega un nuevo servicio a un cliente recurrente
# No sobrescribe el archivo, solo añade información
# --------------------------------
def add_service_to_existing_client():    
    name = input("Nombre del cliente: ").strip()

    if not name:
        print("Nombre invalido.")
        return

    path = client_path(name)

    if not os.path.exists(path):
        print("El cliente no existe.")
        return

    service = input("Nuevo servicio (telefonía/internet/tv de paga): ").strip()
    desc = input("Descripcion del nuevo servicio: ").strip()

    # Agrega información al archivo existente
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"- [{now_str()}] {service} | {desc}\n")

    print("Solicitud agregada correctamente.")


# --------------------------------
# Función: ver expediente de un cliente
# Muestra el contenido completo del archivo del cliente en pantalla
# --------------------------------
def view_client_file():    
    name = input("Nombre del cliente: ").strip()

    if not name:
        print("Nombre invalido.")
        return

    path = client_path(name)

    if not os.path.exists(path):
        print("El cliente no existe.")
        return

    print("\n=== Expediente del Cliente ===")
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())


# --------------------------------
# Función: listar todos los clientes
# Muestra una lista de los archivos de clientes registrados
# Cada cliente es un archivo .txt
# --------------------------------
def list_clients():    
    files = [f for f in os.listdir(CLIENTS_DIR) if f.endswith(".txt")]

    if not files:
        print("No hay clientes registrados.")
        return

    print("=== Lista de clientes ===")
    for f in files:
        print(f"- {f}")


# --------------------------------
# Función: buscar cliente por nombre
# Permite buscar un cliente por su nombre 
# --------------------------------
def find_client():    
    name = input("Nombre del cliente a buscar: ").strip()

    if not name:
        print("Nombre invalido.")
        return

    path = client_path(name)

    if os.path.exists(path):
        print("Cliente encontrado.")
    else:
        print("Cliente no encontrado.")