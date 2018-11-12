
# Ranking Hope for Salem 2018


![](img/10KMedia-Slide-16-9-2018.png)


## Presentació

Aquest repositori conté la pràctica  de _web scraping_ de l´assignatura __"Tipología i cicle de vida de les dades"__ del 
[Màster en Ciència de Dades de la UOC](https://estudios.uoc.edu/es/masters-universitarios/data-science/presentacion).

L´objectiu principal d´aquesta pràctica és elaborar un cas pràctic orientat a aprendre a identificar les dades rellevants per un projecte analític i usar les eines d´extracció de dades.

En particular, s´ha realitzat _web scraping_ a la pàgina __Huber Timing__[^1] en
la que es poden consultar les classificacions i els temps de curses de _running_. En
aquest sentit s´han obtingut les dades de la cursa 10K solidària __Hope For Salem 2018__[^2].


[^1]: http://www.hubertiming.com/
[^2]: https://ugmsalem.org/walkforhope/


## Fitxers de codi font

La documentació generada en la realització de la pràctica es troba allotjada en GitHub al següent repositori:

* https://github.com/rsanchezs/web-scraping

En aquest repositori es poden trobar els següents fitxers


* **src/scraper.py:** conté el _scraper_ que obté el conjunt de dades.
* **data/ranking.csv:** arxiu CSV amb el conjunt de dades.

Per altra banda, també es pot visitar el següent [enllaç](https://rsanchezs.github.io/web-scraping/) que conté la mateixa
documentació que aquest document:

* https://rsanchezs.github.io/web-scraping/


## Requisits

La implementació del _scraper_ s´ha realitzat amb la versió 3.7.0 de Python. Si
és necessari caldrà instal.lar els següents mòduls, per exemple s´utilitzem
`pip3`:

```{}
pip3 install beautifulsoup
pip3 install requests
pip3 install html5lib
```

## Resumen

La extracció de les dades ha sigut realitzada per Rubén Sánchez Sancho de la web  __Huber Timing__. Aquest conjunt de dades correspon a les classificacions en la carrera __Hope For Salem 2018__.

| __Característiques conjunt de dades__  | <span style="font-weight:normal">Análisis multivarible, Series Temporales</span>  |  __Nombre observacions__ | <span style="font-weight:normal">129</span> | __Area__  | <span style="font-weight:normal">Social, Esports </span> |
|---|---|---|---|---|---|
| __Característiques atributs__  | Enteros, Real, Categòriques  | __Nombre atributs__  |14 | __Dates obtingudes__  | 12/11/2018  |
| __Tasques asociades__  | Classificació, Regresió  | __Valors desconeguts?__  | Sí  | __Nombre de webs consultades__  | 1 |



## Informació del conjunt de dades


Aquest conjunt de dades consta de 15 variables i 129 observacions. Els tipus dels
atributs són els següentes:

* **Numèriques:**

  + **Discretes:** `Chip Time`, `Chip Pace`, `Time to Start`, `Gun Time`
  + **Continues:** `Place`, `Bib`, `Age`, `Age Group`, `Age Group Place`  
  
* **Categòriques:** `Gender`, `City, State`

La variable continua `Gender Place` està agrupada en classes on la marca de classe es 9. Les variables `Gender Place` i `Age Group Place` són les posicions respecte el total i estàn representades per un _string_.

Per acabar, s´ha de tenir en compte que els atributs poden contindré valors desconeguts.


## Informació dels atributs


| __Atribut__  | __Descripció__   | 
|:-:|:-:| 
| __Place__  | Classificació general  | 
|  __Bib__ |  Dorsal del runner | 
|  __Name__ |  Nom i cognoms del runner | 
|   __Gender__| Gènere del runner  | 
| __Age__ | Edat del runner | 
| __City__  |  Ciutat  del runner|
| __State__  | Estat de la ciutat  |
|  __Chip Time__ |  Temps calculat pel chip |
| __Chip Pace__  | Ritme enregistrat pel chip  |
| __Gender Place__  | Posició obtinguda respecte gènere  |
|  __Age Group__ | Posició obtinguda respecte interval edat  |
| __Age Group Place__  | Posició obtinguda en la mateixa edad  |
| __Time to Start__  | Temps sortida carrera  |
|  __Gun Time__ | Gun time = Chip time - time to start  |
| __Team__ | Equip al que pertany el runner |


## Origen de les dades

[HUBR TIMING - Race Timing Servide](http://www.hubertiming.com/home)

HUBER TIMING, LLC. Copyright 2009 - 2018

e-mail: timing@hubertiming.com  

## Llicència



<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://rsanchezs.github.io/web-scraping/">
    <span property="dct:title">Ruben SANCHEZ SANCHO</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Ranking  Hope for Salem 2018 | Pràctica web scraping assignatura Tipología i cicle de vida de les dades de la UOC</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="ES" about="https://rsanchezs.github.io/web-scraping/">
  España</span>.
</p>







