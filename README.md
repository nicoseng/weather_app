# weather_app

Code source : https://github.com/nicoseng/weather_app
Programme rédigé sous Python3. Projet sous Virtual Env et Git

# I°) Préparez l’environnement virtuel de développement

1.	Installez un environnement virtuel de développement depuis votre terminal. (python3 –m venv env) ;
2.	Activez l’environnement virtuel en tapant source env/bin/activate. Une mention (env) s’affiche à gauche de votre console.

# II°) Configurez votre projet 

1.	 Rendez-vous sur le site de OPENWEATHERAPP : https://openweathermap.org/.
2.	 Cliquer dans l'onglet API
3.	 Dans le fichier intitulé app.py, recopiez votre propre clé API à la suite de la variable KEY. Cette clé permet à votre application d'effectuer des requêtes sur OPENWEATHERAPP.

# III°) Démarrez l'application GrandPyBot 

Dans le terminal, entrez heroku open. Cette commande permet de se connecter à l'adresse URL où est hébergé l'application sur heroku : https://grand-pybot.herokuapp.com/


# IV°) Utilisez l'application

L'application permet à l'utilisateur d'entrer le nom d'une ville ou d'un endroit de son choix afin d'y obtenir :

- la localisation exacte de l'endroit en question affichée sur une carte Google Maps ;
- une courte histoire du lieu en question raconté par notre fameux grandpyBot.
