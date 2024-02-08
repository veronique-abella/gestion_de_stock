import mysql.connector
from tkinter import *

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vllmcdpdu.13",
    database="store"
)
cursor = db.cursor()

# Fonction pour ajouter un produit
def add_product():
    name = name_entry.get()
    description = description_entry.get("1.0", END)
    price = price_entry.get()
    quantity = quantity_entry.get()
    category_id = category_entry.get()

    sql = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
    val = (name, description, price, quantity, category_id)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "produit ajouté.")

# Fonction pour afficher les produits
def display_products():
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        print(product)

# Fonction pour supprimer un produit
def delete_product():
    product_id = product_id_entry.get()
    sql = "DELETE FROM product WHERE id = %s"
    val = (product_id,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "produit supprimé.")

# Fonction pour modifier un produit
def update_product():
    product_id = product_id_entry.get()
    new_quantity = new_quantity_entry.get()
    new_price = new_price_entry.get()

    sql = "UPDATE product SET quantity = %s, price = %s WHERE id = %s"
    val = (new_quantity, new_price, product_id)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "produit modifié.")

# Interface graphique
root = Tk()
root.title("Gestion de stock")

# Ajout de produits
Label(root, text="Nom:").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Description:").grid(row=1, column=0)
description_entry = Text(root, height=5, width=30)
description_entry.grid(row=1, column=1)

Label(root, text="Prix:").grid(row=2, column=0)
price_entry = Entry(root)
price_entry.grid(row=2, column=1)

Label(root, text="Quantité:").grid(row=3, column=0)
quantity_entry = Entry(root)
quantity_entry.grid(row=3, column=1)

Label(root, text="ID Catégorie:").grid(row=4, column=0)
category_entry = Entry(root)
category_entry.grid(row=4, column=1)

# Bouton "Ajouter Produit"
Button(root, text="Ajouter Produit", command=add_product).grid(row=5, column=0, columnspan=2, pady=5)

# Bouton "Afficher Produits"
Button(root, text="Afficher Produits", command=display_products).grid(row=5, column=2, pady=5)

# Bouton "Supprimer Produit"
Button(root, text="Supprimer Produit", command=delete_product).grid(row=5, column=3, pady=5)

# Bouton "Modifier Produit"
Button(root, text="Modifier Produit", command=update_product).grid(row=5, column=4, pady=5)

# Suppression de produit
Label(root, text="ID du produit à supprimer:").grid(row=6, column=0)
product_id_entry = Entry(root)
product_id_entry.grid(row=6, column=1)

# Modification de produit
Label(root, text="ID du produit à modifier:").grid(row=7, column=0)
product_id_entry = Entry(root)
product_id_entry.grid(row=7, column=1)

Label(root, text="Nouvelle Quantité:").grid(row=7, column=2)
new_quantity_entry = Entry(root)
new_quantity_entry.grid(row=7, column=3)

Label(root, text="Nouveau Prix:").grid(row=7, column=4)
new_price_entry = Entry(root)
new_price_entry.grid(row=7, column=5)

root.mainloop()
