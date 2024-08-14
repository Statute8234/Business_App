import sqlite3
from cryptography.fernet import Fernet
import os

# path
db_path = 'business_database.db'
keys_path = 'keys/'
os.makedirs(keys_path, exist_ok=True)
# Load or generate encryption keys
def load_or_generate_key(filename):
    key_file = os.path.join(keys_path, filename)
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return Fernet(f.read())
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
        return Fernet(key)
db_cipher = load_or_generate_key('db_key.key')
pwd_cipher = load_or_generate_key('pwd_key.key')
# create database
def create_database():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS business_users
             (id INTEGER PRIMARY KEY, business_name TEXT, username TEXT, email TEXT, password TEXT)''')
        conn.commit()
        conn.close()
# encrypt
def encrypt_db():
    with open(db_path, 'rb') as file:
        data = file.read()
    encrypted_data = db_cipher.encrypt(data)
    with open(db_path, 'wb') as file:
        file.write(encrypted_data)
# decrypt
def decrypt_db():
    with open(db_path, 'rb') as f:
        encrypted_data = f.read()
    data = db_cipher.decrypt(encrypted_data)
    with open(db_path, 'wb') as f:
        f.write(data)
# add user
def add_user(business_name, username, email, password):
    decrypt_db()  # Decrypt the database before adding a user
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    encrypted_email = pwd_cipher.encrypt(email.encode())
    encrypted_password = pwd_cipher.encrypt(password.encode())
    cur.execute("INSERT INTO business_users (business_name, username, email, password) VALUES (?, ?, ?, ?)",
                (business_name, username, encrypted_email, encrypted_password))
    conn.commit()
    conn.close()
    encrypt_db()  # Encrypt the database after the operation
# edit user
def edit_user(user_id, business_name=None, username=None, email=None, password=None):
    decrypt_db()
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    if email and password:
        encrypted_email = pwd_cipher.encrypt(email.encode())
        encrypted_password = pwd_cipher.encrypt(password.encode())
        cur.execute("UPDATE business_users SET business_name=?, username=?, email=?, password=? WHERE id=?",
                    (business_name, username, encrypted_email, encrypted_password, user_id))
        conn.commit()
    conn.close()
    encrypt_db()
# show users
def show_all_users():
    decrypt_db()
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM business_users")
    users = cur.fetchall()
    for user in users:
        #decrypted_email = pwd_cipher.decrypt(user[3]).decode()
        #decrypted_password = pwd_cipher.decrypt(user[4]).decode()
        print(f"ID: {user[0]}, Business Name: {user[1]}, Username: {user[2]}, Email: {decrypted_email}, Password: {decrypted_password}")
    conn.close()
    encrypt_db()
# clear database
def clear_db():
    decrypt_db()
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM business_users")
    conn.commit()
    conn.close()
    encrypt_db()
    print("Database cleared.")

if __name__ == "__main__":
    create_database()
    #add_user(business_name="test", username="username", email="test_email", password="password")
    show_all_users()
    clear_db()
