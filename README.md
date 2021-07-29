# Ejercicio - Investigación / Script
Ejercicio de script para el Test Gestión Operativa - Básico

## Table of contents
* [General info](#general-info)
* [How it works](#how-it-works)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
The script allows to generate a file with the publications of a Mercado Libre Argentina seller knowing their selled_id, in case of not knowing it, the following script can be used to obtain it https://github.com/GCE140/obtener_id_usuario_MELI.

## How it works
This program works by making a query to the Mercado Libre API corresponding to searches for more than a thousand items from a seller (https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas#Trabajar-con-Scan-Hash).

For this type of query you need a Mercado Libre app (https://developers.mercadolibre.com.ar/es_ar/mi-primera-aplicacion#Crea-una-aplicacion-en-Mercado-Libre), with it it will be possible to obtain the authentication to use the API.

The program uses the App ID, the Client Secret and the generated Code to consult the Mercado Libre API and generate a token according to what is specified in https://developers.mercadolibre.com.ar/es_ar/autenticacion-y-autorizacion.

The results are saved in a text file in the same location where the script is found, having the following format:

* Artículo x: 
* ID del ítem: MLAXXXXXXXXX 
* Título del ítem: XXXXXXXXXXXXXXXXXX 
* ID de la catgoría del ítem: MLAXXXXXX 
* Nombre de la categoría: MLA-XXXXXXXXXXXX
	
## Technologies
Project is created with:
* Python 3.9
* requests 2.26.0
* requests-oauthlib
	
## Setup
To run this project, install locally:

* pip install requests
* pip install requests-oauthlib
