import sqlite3
from django.shortcuts import render, redirect, reverse
from breadapp.models import Bread
from ..connection import Connection

def bread_list(request): 
    if request.method == 'GET': 
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
            b.id,
            b.name, 
            b.region
            FROM breadapp_bread b
            ORDER BY b.name ASC
            """)
            all_breads = []
            dataset = db_cursor.fetchall()

            for row in dataset: 
                bread = Bread()
                bread.id = row["id"]
                bread.name = row["name"]
                bread.region = row["region"]

                all_breads.append(bread)

    template = "breads/list.html"
    context = {
        'breads': all_breads
    }
    return render(request, template, context)