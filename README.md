# API-testaus

Tämä projekti sisältää vinkkejä API-testaukseen erilaisilla työkaluilla.

# Schemathesis

[Schemathesis](https://schemathesis.readthedocs.io/en/stable/) on avoimen lähdekoodin testaus- ja validointityökalu, joka on suunniteltu API-rajapintojen testaamiseen [OpenAPI](https://www.openapis.org/)- ja [GraphQL](https://graphql.org/)-spesifikaatioiden pohjalta. Työkalu käyttää ns. property-based testing -lähestymistapaa, mikä tarkoittaa, että se generoi automaattisesti suuria määriä erilaisia testitapauksia spesifikaation määrittelemien sääntöjen mukaisesti, ja pyrkii näin löytämään virheitä API:n toiminnassa esimerkiksi erilaisten reunatapausten ja virhetilanteiden avulla. Schemathesis hyödyntää Pythonin [Hypothesis-kirjastoa](https://github.com/HypothesisWorks/hypothesis) ominaisuusperustaiseen testaukseen, ja se on helppo integroida CI/CD-putkiin, sillä se soveltuu jatkuvaan testaamiseen esim. GitHub Actionsissa.

Schemathesis-työkalun dokumentaatiosivuilla on hyvä [tutoriaali](https://schemathesis.readthedocs.io/en/stable/tutorials/cli/), jonka avulla voit opiskella työkalun käyttöä komentoriviltä. Hieman edistyneempi [tutoriaali](https://schemathesis.readthedocs.io/en/stable/tutorials/pytest/) puolestaan näyttää, miten Schemathesis voidaan integroida [pytest-testauskirjastoon](https://docs.pytest.org/en/stable/).

# Projektin asennus

Tässä repossa on esimerkkiskripti, joka testaa [lemmikkieläinkaupan APIa](https://petstore3.swagger.io/) käyttäen Schemathesis-työkalua.

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
Tämä asentaa Schemathesis-työkalun sekä [pytest](https://docs.pytest.org/en/stable/)-kirjaston.

# Testien ajo

Aja schemathesis_tests -kansiossa:

```
pytest test_api.py
```