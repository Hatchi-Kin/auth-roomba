
## Setup

```bash
# Clone the repository
git clone https://github.com/Hatchi-Kin/auth-roomba.git

# Navigate into the project directory
cd auth-roomba

# Create a Python virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py

```

## Usage

Pour utiliser l'app:

 - Se créer un compte et se log in.
 - Créer un 'checkpoint' en entrant l'url de l'ics qui vous concerne <br>
 (example: https://web.isen-ouest.fr/*************.ics )
 - L'app peut maintenant afficher le contenu du calendrier ics. Les événements qui diffèrent du checkpoint seront affichés en rouge.


## Structure

```bash
.
│   app.py                            # Le script Python principal de l'application.
│   docker-compose.yml                # Pour deployer dans un contenaeur -> docker-compose up -d
│   Dockerfile
│   README.md                         # Vous êtes ici !
│   requirements.txt
│
├───instance
│       database.db                   # BDD SQLite pour authentification et checkpoint
│
├───static
│       23_24_CODE_BZH_MICROSOFT_BREST_ALT.ics   # exemple de .ics
│       pico.css                      # Mini framework css pour le moins de front possible !
│       Screenshot-TEMPLATE.png
│
├───templates
│       base.html
│       dashboard.html
│       home.html
│       login.html
│       register.html
│
└───website
        forms.py                      # .py contenant les classes pour les formulaires
        models.py                     # .py contenant les classes pour l'authentification
        routes.py                     # .py contenant toutes les routes de l'app
        utils.py                      # .py contenant toutes les fontions utiles à l'app
```

## Roomba perso !

![Image](https://raw.githubusercontent.com/Hatchi-Kin/auth-roomba/main/static/Screenshot-TEMPLATE.png)
