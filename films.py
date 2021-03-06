from tkinter import *
from tkinter import ttk

import requests

APIKEY = "e14229bc"
URL = "http://www.omdbapi.com/?s={}&apikey={}"

class Searcher(ttk.Frame):

    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent)

        lblSearcher = ttk.Label(self, text="Film:")
        self.ctrSearcher = StringVar()
        txtSearcher = ttk.Entry(self, width=30, textvariable=self.ctrSearcher)
        btnSearcher = ttk.Button(self, text="Search", command=lambda: command(self.ctrSearcher.get()))

        lblSearcher.pack(side=LEFT)
        txtSearcher.pack(side=LEFT)
        btnSearcher.pack(side=LEFT)

    def click(self):
        print(self.ctrSearcher.get())

class Controller(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=400, height=550)
        self.grid_propagate(False)
        
        self.searcher = Searcher(self, self.busca)
        self.searcher.grid(column=0, row=0)

        self.film = Film(self)
        self.film.grid(column=0, row=1)

    def busca(self, peli):
        print(peli, "desde el controller")

        url = URL.format(peli, APIKEY)
        results = requests.get(url)

        if results.status_code == 200:
            films = results.json()
            if films.get("Response") == "True":
                peli_primera = films.get("Search")[0]
                la_peli = {"titulo": peli_primera.get("Title"), "year": peli_primera.get("Year"), "poster": peli_primera.get("Poster")}
                self.film.encontrada = mi_peli


        else:
            pass

        print(results.text)

class Film(ttk.Frame):
    

    def __init__(self, parent):
        __encontrada = None
        ttk.Frame.__init__(self, parent)

        self.lblTitle = ttk.Label(self, text="Titulo")
        self.lblYear = ttk.Label(self, text=1900)

        self.lblTitle.pack(side=TOP)
        self.lblYear.pack(side=TOP)

    @property # GETTER - SI YO LE PIDO, EL ME LO DA
    def encontrada(self):
        return self.__encontrada

    @encontrada.setter
    def encontrada(self, value):
        self.__encontrada = value
        
        self.lblTitle.config(text=self.__encontrada.get("titulo"))
        self.lblYear.config(text=self.__encontrada.get("year"))


