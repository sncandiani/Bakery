import sqlite3
from django.shortcuts import render, redirect, reverse
from breadapp.models import Bread, Ingredient
from ..connection import Connection

# Gets specific bread based on bread ID
# def get_bread(bread_id): 
#         with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()
#             db_cursor.execute("""
#             SELECT
#             b.id as bread_id,
#             b.name, 
#             b.region
#             FROM breadapp_bread as b
#             WHERE b.id = ?
#             """, (bread_id,))
#         return db_cursor.fetchone()

def get_bread_ingredients(bread_id): 
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute("""
            SELECT
            b.id as bread_id,
            b.name as bread_name, 
            b.region, 
            bi.id, 
            bi.amount, 
            i.id as ingredient_id,
            i.name as ingredient_name
            FROM breadapp_bread as b
            JOIN breadapp_breadingredient as bi
            ON b.id = bi.bread_id
            JOIN breadapp_ingredient as i 
            ON i.id = bi.ingredient_id 
            WHERE b.id = ?
            """, (bread_id,))
        dataset =  db_cursor.fetchall()
        bread = Bread()
        bread.list_ingredients = []
        bread.name = dataset[0]["bread_name"]
        bread.region = dataset[0]["region"]
        for row in dataset: 
            ingredient = Ingredient()
            ingredient.id = row['ingredient_id']
            ingredient.name = row['ingredient_name']
            ingredient.amount = row['amount']
            bread.list_ingredients.append(ingredient)

        return bread

# def get_bread_ingredients(bread_id): 
#     with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()
#             db_cursor.execute("""
#             SELECT
#             b.id as bread_id, 
#             b.name, 
#             b.region,
#             bi.id,
#             bi.amount,
#             i.name AS ingredient_name
#             FROM breadapp_bread as b
#             JOIN breadapp_breadingredient as bi
#             ON b.id = bi.bread_id
#             JOIN breadapp_ingredient as i
#             ON i.id = bi.ingredient_id
#             WHERE b.id = ?
#             """, (bread_id,))
            
    # response = db_cursor.fetchone()
    # for row in response: 
    #     ingredient = Ingredient()
    #     ingredient.name = row['ingredient_name']
    #     ingredient.amount = row['amount']


    # return ingredient

    

# Uses specific bread method as context in order to display details using the template 
def bread_details(request, bread_id): 
    if request.method == 'GET': 
        bread = get_bread_ingredients(bread_id)
        template = "breads/detail.html"
        context = {
            'bread': bread
        }
        return render(request, template, context)