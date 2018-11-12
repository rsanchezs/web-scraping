
# Pràctica 1: Web scraping

![](img/hope_for_salem_10k_2018.jpg)


## Presentació

Aquest repositori conté la pràctica  de _web scraping_ de l´assignatura __"Tipología i cicle de vida de les dades"__ del 
[Màster en Ciència de Dades de la UOC](https://estudios.uoc.edu/es/masters-universitarios/data-science/presentacion).

L´objectiu principal de aquesta pràctica és elaborar un cas pràctic orientat a aprendre a identificar les dades rellevants per un projecte analític i usar les eines d´extracció de dades.

En particular, s´ha realitzat _web scraping_ a la pàgina __Huber Timing__[^1] en
la que es poden consultar les classificacions i els temps de curses de _running_. En
aquest sentit s´han obtingut les dades de la cursa 10K solidaria __Hope For Salem 2018__[^2].


[^1]: http://www.hubertiming.com/
[^2]: https://ugmsalem.org/walkforhope/


## Fitxers de codi font

* **src/scraper.py:** conté el _scraper_ que obté el conjunt de dades.
* **data/ranking.csv:** arxiu CSV amb el conjunt de dades.

## Requisits

La implementació del _scraper_ s´ha realitzat amb la versió 3.7.0 de Python. A més,
si és necessari caldrà instal.lar els següents moduls, per exemple s´utilitzem
`pip3`:

```{}
pip3 install beautifulsoup
pip3 install requests
pip3 install html5lib
```




