# weather_app

Code source : https://github.com/nicoseng/weather_app
Programme rédigé sous Python3. Projet sous Virtual Env et Git

# I°) Préparez l’environnement virtuel de développement

1.	Installez un environnement virtuel de développement depuis votre terminal. (python3 –m venv env) ;
2.	Activez l’environnement virtuel en tapant source env/bin/activate. Une mention (env) s’affiche à gauche de votre console.

# II°) Configurez votre projet 

1.	 Rendez-vous sur le site de OPENWEATHERAPP : https://openweathermap.org/.
2.	 Cliquez dans l'onglet API et générer votre clé API ;
3.	 Dans Current & Forecast weather data collection, souscrivez à l'abonnement Current Weather Data en cliquant sur le bouton subscribe ;
4.	 Choissisez la formule FREE en cliquant sur Get API key ;
5.	 Créez votre compte si besoin ;
6.	 Cliquez sur l'onglet API keys ;
7.	 Dans la rubrique Create key, donnez un nom à votre API puis cliquez sur le bouton generate ;
8.	 Copiez votre clé API ;
9.	 Dans le fichier intitulé ow_api.py, collez votre propre clé API entre les guillemets. Cette variable KEY permet à votre application d'effectuer des requêtes sur OPENWEATHERAPP.

# III°) Démarrez l'application WeatherApp

Dans le terminal, entrez flask run.


# IV°) Utilisez l'application

L'application permet à l'utilisateur d'entrer le nom d'une ville ou d'un endroit de son choix afin d'y obtenir :

- La météo générale de la ville en question ;
- Le pays correspondant à la ville recherchée.
