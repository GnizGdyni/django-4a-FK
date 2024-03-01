# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('''

    <button onclick="inc">Hello World</button>
    <br><br>
    <input></input>
    <br><br>
    <select></select>
        <script>
    var inc = function() {
        alert("yooo")
    }

    </script>
    ''')

def counter(request):
    text_file = open("./templates/fv.html","r")
    page = text_file.read()
    text_file.close()
    # page = "fggdd"
    print(page)
    return HttpResponse(page)

def basic(request):
    text_file = open("./templates/home.html","r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)