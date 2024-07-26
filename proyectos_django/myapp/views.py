from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    html = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Curson V2</title>
            <style>
                table, th, td {
                border:1px solid black;
                }
                </style>
        </head>
        <body style="background-color:blueviolet;">
            <p style="color: white; font-size: 50px; text-align: center;">
                Esta es una pagina diferentes 
                <a href="index_2">click aqui</a>
            </p>
            <p>
                ver mas ejemplos en  <a href="https://www.w3schools.com/html/default.asp">W3School</a>

            </p>
            <ol>
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ol>  
            
        <table style="width:100%">
            <tr>
            <th>Company</th>
            <th>Contact</th>
            <th>Country</th>
            </tr>
            <tr>
            <td>tienda A</td>
            <td>Maria Anders</td>
            <td>Germany</td>
            </tr>
            <tr>
            <td>tienda B</td>
            <td>Francisco Chang</td>
            <td>Mexico</td>
            </tr>
        </table>
        
        </body>
        </html>

    """
    return HttpResponse(html)


def index_2(request):
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Curson V2</title>
        </head>
        <body style="background-color:blueviolet;">
            <p style="color: white; font-size: 50px; text-align: center;">
                Hola curso de Django
                <a href="index">
                    Volver al inicio 
                </a>
            </p>

        </body>
        </html>
    """
    return HttpResponse(html)
