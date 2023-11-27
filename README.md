## :robot: Auth-Roomba  

Cette web app Flask, permet à un utilisateur, une fois connecté, de créer un "checkpoint" en entrant l'URL d'un calendrier ICS. L'application peut ensuite afficher le contenu du calendrier et alerter des événements qui ont été ajoutés ou modifiés depuis le dernier checkpoint.

## :building_construction: Setup   

Dans un environment virtuel:

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

Dans un container Docker:

```bash
# Clone the repository
git clone https://github.com/Hatchi-Kin/auth-roomba.git

# Navigate into the project directory
cd auth-roomba

# Build and run the the container in the background
docker compose-up -d

# Then go to localhost:5001

```


## :calendar: Usage  

Pour utiliser l'app:

 - Se créer un compte et se log in.
 - Créer un 'checkpoint' en entrant l'url de l'ics qui vous concerne <br>
 (example: https://web.isen-ouest.fr/*************.ics )
 - L'app peut maintenant afficher le contenu du calendrier ics. Les événements qui diffèrent du checkpoint seront affichés en rouge.


## :deciduous_tree: Structure  

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
        utils.py                      # .py contenant toutes les fonctions utiles à l'app
```

## :pager: Roomba perso ! 
![Image](https://raw.githubusercontent.com/Hatchi-Kin/auth-roomba/main/static/Screenshot-TEMPLATE.png)
