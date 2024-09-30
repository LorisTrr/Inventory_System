-- Créer la base de données
CREATE DATABASE IF NOT EXISTS inventory_system;

-- Utiliser la base de données
USE inventory_system;

-- Créer la table 'utilisateurs'
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telephone VARCHAR(15),
    mot_de_passe VARCHAR(255) NOT NULL,
    est_admin BOOLEAN DEFAULT FALSE,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Créer la table 'inventaire'
CREATE TABLE IF NOT EXISTS inventaire (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL,
    quantite INT NOT NULL,
    date_ajout DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertion de données dans la table 'utilisateurs'
INSERT INTO utilisateurs (nom, prenom, email, telephone, mot_de_passe, est_admin) VALUES
('Dupont', 'Jean', 'jean.dupont@example.com', '0123456789', 'hashed_password_1', TRUE),
('Martin', 'Sophie', 'sophie.martin@example.com', '0987654321', 'hashed_password_2', FALSE),
('Durand', 'Lucas', 'lucas.durand@example.com', '0147258369', 'hashed_password_3', FALSE);

-- Insertion de données dans la table 'inventaire'
INSERT INTO inventaire (nom, prix, quantite) VALUES
('Produit A', 19.99, 50),
('Produit B', 29.99, 30),
('Produit C', 9.99, 100),
('Produit D', 49.99, 20);
