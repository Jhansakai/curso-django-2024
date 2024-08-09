from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product, Person, Carrito

# Create your views here.


def get_productos(request):
    porductos = Product.objects.all()
    context = {
        "numero_productos": len(porductos),
        "productos": porductos,
    }
    return render(request, "myapp/productos_list.html", context)


def get_customers(request):
    clientes = Person.objects.all()
    context = {
        "numero_clientes": len(clientes),
        "clientes": clientes,
    }
    return render(request, "myapp/customer_list.html", context)

def get_carritos(request):
    carritos = Carrito.objects.all()
    context = {
        "numero_carritos": len(carritos),
        "carritos": carritos,
    }
    return render(request, "myapp/carrito_list.html", context)

def get_carrito_detail(request, id):
    carrito = Carrito.objects.filter(id=id).first()
    productos = carrito.productos.all()
    context = {
        "carrito": carrito,
        "numero_productos": len(productos),
        "productos": productos,
    }
    return render(request, "myapp/carrito_detail.html", context)



def index(request):
    context = {
    }
    return render(request, "myapp/index.html", context)


def index_2(request):
    porductos = Product.objects.all()
    productos_base_html = """
        <div class="col-sm-4">
            <h3>{}</h3>
            <p>{}</p>
            <p>{}</p>
        </div>
    """
    productos_list_html = ""
    for producto in porductos:
        productos_list_html = productos_list_html + productos_base_html.format(
            producto.product_name, producto.description, producto.sell_price
        )
    
    
    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>

    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Logo</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
            <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="/page_2">About</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#">Contacto</a>
            </li>  
            <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Proyectos</a>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Home</a></li>
                <li><a class="dropdown-item" href="#">Another link</a></li>
                <li><a class="dropdown-item" href="#">A third link</a></li>
            </ul>
            </li>
        </ul>
        </div>
    </div>
    </nav>

    <div class="container-fluid p-5 bg-primary text-white text-center">
    <h1>Pagina de Productos</h1>
    <p>vamos a visualizar {} productos registrados en la base de datos</p> 
    </div>
    
    <div class="container mt-5">
    <div class="row">
        {}
    </div>
    </div>

    </body>
    </html>
""".format(len(porductos), productos_list_html)
    return HttpResponse(html)


def index_3(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Logo</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavbar">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Contacto</a>
        </li>  
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Proyectos</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Home</a></li>
            <li><a class="dropdown-item" href="#">Another link</a></li>
            <li><a class="dropdown-item" href="#">A third link</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>

<div class="container-fluid p-5 bg-primary text-white text-center">
  <h1>este es el about</h1>
  <p>Resize this responsive page to see the effect!</p> 
</div>
  
<div class="container mt-5">
  <div class="row">
    <div class="col-sm-4">
      <h3>Comentario 1</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>Comentario 2</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
    <div class="col-sm-4">
      <h3>Comentario 3</h3>        
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
      <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
    </div>
  </div>
</div>

</body>
</html>



    """
    return HttpResponse(html)
