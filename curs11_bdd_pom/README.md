# Gerkin project

### Creare proiect

Creare proiect nou in PyCharm, cu virtualenv alocat.
Proiectul va avea si un repository pe Github-ul vostru.

### Pre-requisites

Se instaleaza cu `pip install <nume librarie>`

* behave
* behave-html-formatter
* selenium
* webdriver-manager


### Structura foldere si fisiere

```
/features
    /login.feature -- aici sunt de fapt testele noastre in limbaj Gherkin
    /signup.feature
    /ceva.feature
    /steps
        /login.py -- aici sunt implementati pasii din login feature
        /signup.py
        /ceva.py
    /browser.py -- aici facem clasa Browser
    /environment.py -- aici setam hooks care pun browserul in context
behave.ini -- fisier de config pentru html formatter
```