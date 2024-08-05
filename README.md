# Projet VSTROM

## Objectif

L'objectif ici est d'échanger sur certains concepts techniques autour de Django, Bootstrap, HTMX, Docker et d'autres à venir.

C'est une maquette réalisée rapidement pour mettre en oeuvre quelques concepts techniques


## Fait

* mise en oeuvre de l'héritage de template
* mise en oeuvre des filtres de template
* mise en oeuvre de la sécurité CSRF
* mise en oeuvre de Bootstrap
* Mise en oeuvre de CBV (Class-based views)
* Mise en oeuvre de la localisation (EN, FR)
* Mise en oeuvre de "prefetch_related"
* Mise en oeuvre de HTMX pour le chargement de listes liées sans rechargement de page
* Provisionnement de la BDD via fichier CSV via migration Django


## A faire

* Mis en évidence de "select_related" pour résoudre la problématique de requêtes N+1
* Mise en oeuvre de Django REST Framework
* Mise en oeuvre de Vue.js (via Django REST Framework)
  * Configurer les modèles, les sérialiseurs et les vues pour définir une API d'authentification
  * Ajouter les URLs d'API pour l'authentification (connexion, déconnexion, inscription)
  * Configurer les paramètres de Django pour inclure JWT et CORS
  * Configurer Webpack pour l'intégration avec Django
  * Créer un service d'authentification dans Vue.js pour gérer les appels API (connexion, déconnexion, inscription)
  * Développer des composants Vue.js pour l'inscription, la connexion et la déconnexion
  * Utiliser le service d'authentification dans les composants Vue.js pour gérer les opérations d'authentification
* Conteneurisation via Docker Compose avec Nginx + certificats auto générés






