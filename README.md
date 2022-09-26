# TikZ tutorial

## Projekt infók

* [Honlap](https://tikz.agondolkodasorome.hu)
* [PDF](https://a-gondolkodas-orome.github.io/tikz-tutorial/mainpage.pdf)
* [Github link](https://github.com/a-gondolkodas-orome/tikz-tutorial)
* main.tex: [`./src/mainpage.tex`](https://github.com/a-gondolkodas-orome/tikz-tutorial/blob/main/src/mainpage.tex)
* css: [`./css/tikz.css`](https://github.com/a-gondolkodas-orome/tikz-tutorial/blob/main/css/tikz.css)
* logo: [`./img/logo.png`](https://github.com/a-gondolkodas-orome/tikz-tutorial/blob/main/img/logo.png)
* fordítás: `python3 ./build_html.py`
* index.html: `gh-pages` branch: [`./index.html`](https://github.com/a-gondolkodas-orome/tikz-tutorial/blob/gh-pages/index.html), lokálisan: `./docs/index.html`
  * A publikus oldalt egy github action hozza létre a `gh-pages` branchen ([`./.github/workflows/main.yml`](https://github.com/a-gondolkodas-orome/tikz-tutorial/blob/main/.github/workflows/main.yml))

## Dokumentációk
* [Lwarp package](https://ctan.ijs.si/tex-archive/macros/latex/contrib/lwarp/lwarp.pdf)
* [Lwarp example](https://people.bath.ac.uk/feb/lwarp/lwarp-intro.html)
* [Minted package](http://tug.ctan.org/macros/latex/contrib/minted/minted.pdf)

## Megjegyzések

* Egy weblap megfelel egy `\chapter`-nek (ezt a FileDepth definiálja).
* Új fájl esetén kötelező, hogy `\chapter{title_of_chapter}` paranccsal kezdődjön a fájl. 
* Egy új oldalt a `./src/mainpage.tex` fájlban kell meghívni: `\include{name_of_file}`.
* (?) A címekben egyes ékezet helyett a  '<karakter>-t kell használni.
