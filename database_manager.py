import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.connection = self.create_connection(host_name, user_name, user_password, db_name)

    def create_connection(self, host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=db_name
            )
            if connection.is_connected():
                print("Connexion réussie à la base de données MySQL")
        except Error as e:
            print(f"Erreur lors de la connexion à MySQL : {e}")
        return connection

    def get_products(self):
        if self.connection is None:
            print("Erreur : connexion non établie à la base de données.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM produits")  # Remplace 'produits' par le nom de ta table
            products = cursor.fetchall()
            return products
        except Error as e:
            print(f"Erreur lors de la récupération des produits : {e}")
            return None

    def add_product(self, nom, prix, quantite):
        if self.connection is None:
            print("Erreur : connexion non établie à la base de données.")
            return

        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO produits (nom, prix, quantite) VALUES (%s, %s, %s)"
            values = (nom, prix, quantite)
            cursor.execute(query, values)
            self.connection.commit()
            print(f"Produit {nom} ajouté avec succès.")
        except Error as e:
            print(f"Erreur lors de l'ajout du produit : {e}")

    def get_users(self):
        if self.connection is None:
            print("Erreur : connexion non établie à la base de données.")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM utilisateurs")  # Remplace 'utilisateurs' par le nom de ta table
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Erreur lors de la récupération des utilisateurs : {e}")
            return None

    def add_user(self, nom, prenom, email, telephone, mot_de_passe, est_admin, date_creation):
        if self.connection is None:
            print("Erreur : connexion non établie à la base de données.")
            return

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO utilisateurs (nom, prenom, email, telephone, mot_de_passe, est_admin, date_creation)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (nom, prenom, email, telephone, mot_de_passe, est_admin, date_creation)
            cursor.execute(query, values)
            self.connection.commit()
            print(f"Utilisateur {nom} ajouté avec succès.")
        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connexion à la base de données MySQL fermée.")
