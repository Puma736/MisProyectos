import csv
import os
from cryptography.fernet import Fernet

# Archivos donde se guardarán los datos
KEY_FILE = 'secret.key'
CSV_FILE = 'passwords.csv'

# --- Cargar o crear la clave ---
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, 'rb') as key_file:
        key = key_file.read()

cipher_suite = Fernet(key)

# Funciones de cifrado/descifrado
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode('utf-8')

def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode('utf-8')

# --- Crear el CSV si no existe ---
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['website', 'username', 'password'])

#  Cargar contraseñas (en memoria) 
passwords = []
with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)  # saltar encabezado
    for row in reader:
        if len(row) == 3:
            passwords.append({
                "website": row[0],
                "username": row[1],
                "password": row[2]  # cadena cifrada en UTF-8
            })

#  Funciones auxiliares 
def save_all_to_csv():
    """Reescribe todo el CSV con el contenido actual de 'passwords' (preserva valores cifrados)."""
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['website', 'username', 'password'])
        for entry in passwords:
            writer.writerow([entry['website'], entry['username'], entry['password']])

#  Funciones principales 
def add_password():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    encrypted_password = encrypt_password(password)
    passwords.append({
        "website": website,
        "username": username,
        "password": encrypted_password
    })

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([website, username, encrypted_password])
    print("✅ Contraseña guardada correctamente.")

def get_password(website):
    website_query = website.strip().lower()
    found = False
    for entry in passwords:
        if entry['website'].strip().lower() == website_query:
            try:
                decrypted = decrypt_password(entry['password'])
            except Exception:
                decrypted = "<Error: no se pudo descifrar>"
            print(f"\n🔹 Website: {entry['website']}")
            print(f"   Username: {entry['username']}")
            print(f"   Password: {decrypted}\n")
            found = True
    if not found:
        print("❌ Website no encontrado.")

def list_websites():
    if not passwords:
        print("No hay entradas guardadas.")
        return
    print("\nEntradas guardadas:")
    for i, entry in enumerate(passwords, start=1):
        print(f"{i}. {entry['website']}  (user: {entry['username']})")
    print()

def delete_password(website, username):
    website_query = website.strip().lower()
    username_query = username.strip().lower()
    matches = [entry for entry in passwords if entry['website'].strip().lower() == website_query and entry['username'].strip().lower() == username_query]

    if not matches:
        print("❌ No se encontró ninguna entrada con ese website y username.")
        return

    # Mostrar lo que se eliminará
    print("\nSe eliminarán las siguientes entradas:")
    for entry in matches:
        try:
            decrypted = decrypt_password(entry['password'])
        except Exception:
            decrypted = "<Error: no descifrado>"
        print(f"Website: {entry['website']} | Username: {entry['username']} | Password: {decrypted}")

    confirm = input("\n¿Eliminar estas entradas? (s/n): ").strip().lower()
    if confirm not in ('s', 'si', 'y', 'yes'):
        print("Operación cancelada.")
        return

    # Eliminar coincidencias
    passwords[:] = [entry for entry in passwords if not (entry['website'].strip().lower() == website_query and entry['username'].strip().lower() == username_query)]
    save_all_to_csv()
    print("✅ Entradas eliminadas correctamente.")

# --- Menú principal ---
def main():
    while True:
        print("\n1. Add Password")
        print("2. Get Password")
        print("3. Exit")
        print("4. List entries")
        print("5. Delete entry")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_password()
        elif choice == '2':
            website = input("Enter website: ")
            get_password(website)
        elif choice == '3':
            print("Saliendo...")
            break
        elif choice == '4':
            list_websites()
        elif choice == '5':
            website = input("Enter website: ")
            username = input("Enter username: ")
            delete_password(website, username)
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()
