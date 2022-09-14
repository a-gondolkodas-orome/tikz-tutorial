# TikZ tutorial

## Projekt infók

* [Honlap](https://a-gondolkodas-orome.github.io/latex-tutorial/index.html)
* [PDF](https://a-gondolkodas-orome.github.io/latex-tutorial/mainpage.pdf)
* [Github link](https://github.com/a-gondolkodas-orome/latex-tutorial)
* main.tex: ./pages/mainpage.tex
* fordítás (lokálisan): python ./build_html.py 
* index.html: ./docs/index.html 
** A publikus oldalt a deploy github actions csinálja a gh-pages branchen (./.github/workflows/main.yml)

## Dokumentációk
* [Lwarp package](https://ctan.ijs.si/tex-archive/macros/latex/contrib/lwarp/lwarp.pdf)
* [Lwarp example](https://people.bath.ac.uk/feb/lwarp/lwarp-intro.html)
* [Minted package](http://tug.ctan.org/macros/latex/contrib/minted/minted.pdf)

## Megjegyzések

* Egy weblap megfelel egy \chapter-nek (ezt a FileDepth definiálja).
* Új fájl esetén kötelező, hogy \chapter{title_of_chapter} paranccsal kezdődjön a fájl. 
* Egy új oldalt a ./pages/mainpage.tex fájlban kell meghívni: \include{name_of_file}.
* (?) A címekben egyes ékezet helyett a  '<karakter>-t kell használni.
