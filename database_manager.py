import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.create_connection()

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection réussie à la base de données.")
        except Error as e:
            print(f"Erreur de connexion : {e}")
        return connection

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connexion fermée.")

    def get_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM inventaire")
        return cursor.fetchall()

    def add_product(self, nom, prix, quantite):
        cursor = self.connection.cursor()
        query = "INSERT INTO inventaire (nom, prix, quantite) VALUES (%s, %s, %s)"
        values = (nom, prix, quantite)
        cursor.execute(query, values)
        self.connection.commit()
        print("Produit ajouté avec succès !")

    def get_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM utilisateurs")
        return cursor.fetchall()
