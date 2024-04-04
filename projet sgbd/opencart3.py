from tkinter import *
import tkinter as tk
import mysql.connector

# Couleurs
primary_color = "#3498db"  # Bleu
secondary_color = "#ffffff"  # Blanc

# Fonction pour récupérer et afficher la liste des utilisateurs depuis la base de données
def get_user_list():
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="opencartgck"
    )
    cursor = connection.cursor()

    # Exécution de la requête SQL pour récupérer la liste des utilisateurs
    cursor.execute("SELECT username FROM oc_user")
    users = cursor.fetchall()

    # Fermeture de la connexion à la base de données
    cursor.close()
    connection.close()

    # Affichage de la liste des utilisateurs dans une nouvelle fenêtre
    user_list_window = tk.Toplevel(root)
    user_list_window.title("Liste des utilisateurs")

    # Création d'une étiquette pour afficher la liste des utilisateurs
    user_list_label = tk.Label(user_list_window, text="Liste des utilisateurs :", bg=primary_color, fg=secondary_color)
    user_list_label.pack()

    # Affichage de chaque utilisateur dans une étiquette séparée
    for user in users:
        user_label = tk.Label(user_list_window, text=user[0])
        user_label.pack()

# Fonction pour récupérer et afficher les utilisateurs connectés depuis la base de données
def get_online_users():
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="opencartgck"
    )
    cursor = connection.cursor()

    # Exécution de la requête SQL pour récupérer les utilisateurs connectés
    cursor.execute("SELECT username FROM oc_customer_online")
    online_users = cursor.fetchall()

    # Fermeture de la connexion à la base de données
    cursor.close()
    connection.close()

    # Affichage des utilisateurs connectés dans une nouvelle fenêtre
    online_users_window = tk.Toplevel(root)
    online_users_window.title("Utilisateurs connectés")

    # Création d'une étiquette pour afficher les utilisateurs connectés
    online_users_label = tk.Label(online_users_window, text="Utilisateurs connectés :", bg=primary_color, fg=secondary_color)
    online_users_label.pack()

    # Affichage de chaque utilisateur connecté dans une étiquette séparée
    for user in online_users:
        online_user_label = tk.Label(online_users_window, text=user[0])
        online_user_label.pack()

# Fonction pour récupérer et afficher la liste des produits depuis la base de données
def get_product_list():
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="opencartgck"
    )
    cursor = connection.cursor()

    # Exécution de la requête SQL pour récupérer la liste des produits
    cursor.execute("SELECT name, price FROM oc_product")
    products = cursor.fetchall()

    # Fermeture de la connexion à la base de données
    cursor.close()
    connection.close()

    # Affichage de la liste des produits dans une nouvelle fenêtre
    product_list_window = tk.Toplevel(root)
    product_list_window.title("Liste des produits")

    # Création d'une étiquette pour afficher la liste des produits
    product_list_label = tk.Label(product_list_window, text="Liste des produits :", bg=primary_color, fg=secondary_color)
    product_list_label.pack()

    # Affichage de chaque produit dans une étiquette séparée
    for product in products:
        product_label = tk.Label(product_list_window, text=f"Nom: {product[0]}, Prix: {product[1]}")
        product_label.pack()

# Fonction pour vérifier la connexion
def verify_login():
    # Récupérer les données saisies par l'utilisateur
    username = username_entry.get()
    password = password_entry.get()

    # Vérifier si les identifiants correspondent à ceux prédéfinis
    if username == "admin" and password == "admin":
        # Connexion réussie, afficher la page d'accueil
        show_home_page()
    else:
        # Connexion échouée, afficher un message d'erreur
        login_result_label.config(text="Identifiants invalides", fg="red")

# Fonction pour afficher la page d'accueil
def show_home_page():
    # Effacer la fenêtre de connexion
    for widget in root.winfo_children():
        widget.destroy()

    # Afficher le titre de la page d'accueil
    welcome_label = tk.Label(root, text="Bienvenue dans la page d'accueil", bg=primary_color, fg=secondary_color)
    welcome_label.pack()

    # Bouton pour afficher la liste des utilisateurs
    users_button = tk.Button(root, text="Liste des utilisateurs", command=get_user_list, bg=primary_color, fg=secondary_color)
    users_button.pack(pady=5)

    # Bouton pour afficher la liste des utilisateurs connectés
    online_users_button = tk.Button(root, text="Utilisateurs connectés", command=get_online_users, bg=primary_color, fg=secondary_color)
    online_users_button.pack(pady=5)

    # Bouton pour afficher la liste des produits
    products_button = tk.Button(root, text="Liste des produits", command=get_product_list, bg=primary_color, fg=secondary_color)
    products_button.pack(pady=5)

# Code principal
root = tk.Tk()
root.title("Monitoring_OpenCart")
root.config(bg=primary_color)

# Créer les éléments de la fenêtre de connexion
username_label = tk.Label(root, text="Nom d'utilisateur :", bg=primary_color, fg=secondary_color)
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Mot de passe :", bg=primary_color, fg=secondary_color)
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Se connecter", command=verify_login, bg=primary_color, fg=secondary_color)
login_button.grid(row=2, columnspan=2, padx=10, pady=5)

login_result_label = tk.Label(root, text="", bg=primary_color, fg="red")
login_result_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Exécution de la boucle principale Tkinter
root.mainloop()
