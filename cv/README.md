# Como armar el cv


Basado en [pandoc_resume](https://mszep.github.io/pandoc_resume/)

```
pandoc --standalone --from markdown --to pdf --output out/cv.pdf --pdf-engine wkhtmltopdf cv.md
```

```
pandoc --standalone --from markdown --to html --output out/cv.html --css cv/style.css cv.md
```

