import justpy as jp
from webapp.about import About
from webapp.home import Home 
from webapp.dictonary import Dictonary


jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.Route(Dictonary.path, Dictonary.serve)

jp.justpy(port=8001)