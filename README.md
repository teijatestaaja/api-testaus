# API-testaus

Tämä projekti sisältää esimerkkejä API-testaukseen hyödyntäen seuraavia työkaluja ja kirjastoja:
- [Schemathesis](https://schemathesis.github.io/schemathesis/)
- [Hypothesis](https://github.com/HypothesisWorks/hypothesis)-kirjasto
- [pytest](https://docs.pytest.org/en/stable/)-kirjasto
- [requests](https://requests.readthedocs.io/en/latest/)-kirjasto
- [Allure Report](https://allurereport.org/), avoimen lähdekoodin testiraportointityökalu


## Projektin asennus

Tässä repossa on esimerkkiskripti, joka testaa [lemmikkieläinkaupan APIa](https://petstore3.swagger.io/) käyttäen Schemathesis-työkalua, sekä laajentaa testejä pytestillä. Tämä lähestymistapa sisältää siis sekä perinteisen esimerkkipohjaisen testauksen että ominaisuuksiin perustuvan fuzzingin edut.

- Asenna [Python](https://www.python.org/).
- Asenna ja aktivoi [Pythonin virtuaaliympäristö](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) ajamalla tämän repon juuressa Windowsin Git Bashissa:

```
python -m venv testenv
source testenv/Scripts/activate
```

Asenna riippuvuudet:
```
pip install -r requirements.txt
```

Asenna [Allure Report -komentorivityökalu](https://allurereport.org/docs/install/). Esimerkiksi, jos node.js on asennettuna:

```
npm install -g allure-commandline
```

Verifioi asennus:

```
allure --version
```

## Testien ajo

Testit:
- parametrisoidut Schemathesis-testit (test_api.py)
- testi, joka testaa lemmikin luontia (test_pet.py)

Testit ajetaan tests -kansiosta. Aja kaikki testit ja tallenna tulokset JUnit XML-muodossa:

```
pytest -s -v test_api.py test_pet.py --junit-xml=../allure-results/junit-results.xml
```

Generoi ja avaa raportti:

```
allure generate ../allure-results --clean -o ../allure-report
allure open ../allure-report
```

## Opi lisää
- Lyhyt videotutoriaali [PyTest REST API Integration Testing with Python](https://www.youtube.com/watch?v=7dgQRVqF1N0)
- [HTTP statuskoodien selitys](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)