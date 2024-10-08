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
            cursor.execute("SELECT * FROM inventaire")  # Remplace 'produits' par le nom de ta table
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
            query = "INSERT INTO inventaire (nom, prix, quantite) VALUES (%s, %s, %s)"
            values = (nom, prix, quantite)
            cursor.execute(query, values)
            self.connection.commit()
            print(f"Produit {nom} ajouté avec succès.")
        except Error as e:
            print(f"Erreur lors de l'ajout du produit : {e}")

    def delete_product(self, product_id):
        """Supprime un produit de la base de données en fonction de son ID."""
        if self.connection is None:
            print("Erreur : connexion non établie à la base de données.")
            return

        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM inventaire WHERE id = %s"  # Assurez-vous que 'id' est le nom correct de la colonne dans votre table
            cursor.execute(query, (product_id,))  # Ajout d'une virgule pour faire un tuple
            self.connection.commit()
            print(f"Produit avec ID {product_id} supprimé avec succès.")
        except Error as e:
            print(f"Erreur lors de la suppression du produit : {e}")


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

    def delete_user(self, user_id):
        """Supprime un utilisateur de la base de données en fonction de son ID."""
        if self.connection is None:
            print("Erreur : connexion non établie à la base de données.")
            return

        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM utilisateurs WHERE id = %s"  # Remplace 'id' par le nom de la colonne ID dans ta table
            cursor.execute(query, (user_id,))
            self.connection.commit()
            print(f"Utilisateur avec ID {user_id} supprimé avec succès.")
        except Error as e:
            print(f"Erreur lors de la suppression de l'utilisateur : {e}")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connexion à la base de données MySQL fermée.")
