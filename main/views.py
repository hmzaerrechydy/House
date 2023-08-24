from django.shortcuts import render, redirect
from .forms import addContent
import sqlite3

def index(request):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    query = '''SELECT 
                json_group_array(
                json_object(
                'id', id, 
                'title', title, 
                'url', url, 
                'type', type, 
                'topic', topic, 
                'author', author
                )
            )
    FROM list;'''
    cursor.execute(query)
    data = cursor.fetchall()[0][0]

    with open("db.json", "w") as f: 
        f.write(data) 
    
    cursor.close()
    connection.close()

    return render(request, 'frontend/index.html')



def add(request): 
    if request.method == "POST": 
        form = addContent(request.POST)
        if form.is_valid(): 
            data = form.cleaned_data
             
            values = [
                (data["title"]),
                (data["url"]),
                (data["type"]),
                (data["topic"]),
                (data["author"])
            ]

            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()
            query = 'INSERT INTO list (title, url, type, topic,author) VALUES(?,?,?,?,?);'
            cursor.execute(query, values)
            cursor.close()
            connection.commit()
            connection.close()
             
            return redirect("/")
    else: 
        form = addContent()
    return render(request, 'frontend/add.html', {"form": form})