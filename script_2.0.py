import requests, json
from requests.api import request
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
from requests.structures import CaseInsensitiveDict
from datetime import datetime

ahora = datetime.now()
formato_fecha = "%d-%m-%Y-%Hh-%Mm-%Ss"
texto_fecha = ahora.strftime(formato_fecha)

def get_code(client_id, redirect_uri):
    authorization_base_url = f"https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"

    meli = OAuth2Session(client_id)

    authorization_url, state = meli.authorization_url(authorization_base_url)
    print("\nDebes conceder el acceso en:\n\n" + authorization_base_url)

    code = input('\nPega la URL de respuesta completa: ')
    code = code.strip("https://www.mercadolibre.com.ar/?code=")

    print("\nEl código es:\t" + code + "\n")
    return code


def generar_token(app_id, cli_secret, redirect_uri):
    
    code = get_code(app_id, redirect_uri)

    url = "https://api.mercadolibre.com/oauth/token"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["content-type"] = "application/x-www-form-urlencoded"

    data = f"grant_type=authorization_code&client_id={app_id}&client_secret={cli_secret}&code={code}&redirect_uri=https://mercadolibre.com.ar"

    resp = requests.post(url, headers=headers, data=data)

    json_data = json.loads(resp.text)

    print("Reporte de status: " + str(resp.status_code) + "\n")
    print("El token es:\t" + json_data["access_token"] + "\n")
    
    return json_data["access_token"]


def crear_log(token, seller_id):

    url = f"https://api.mercadolibre.com/users/{seller_id}/items/search?search_type=scan"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url, headers=headers)

    print("Reporte de status: " + str(resp.status_code) + "\n")

    if resp.status_code != 200:
        print("Error de acceso al servicio.\n")
    else:
        json_data = json.loads(resp.text)
        print()

        ids = []
        titles = []
        category_ids = []
        domain_ids = []

        for i in range (len(json_data["results"])):
            ids.append(json_data["results"][i]["id"])
            titles.append(json_data["results"][i]["title"])
            category_ids.append(json_data["results"][i]["category_id"])
            domain_ids.append(json_data["results"][i]["domain_id"])

        print("Cantidad de IDs de productos: " + str(len(ids)))
        print("Cantidad de titulos de productos: " + str(len(titles)))
        print("Cantidad de categorías de IDs de productos: " + str(len(category_ids)))
        print("Cantidad de nombres de categorías de productos: " + str(len(domain_ids)))
        print()

        nombre_log = "log_seller_" + seller_id + "_" + texto_fecha

        log = open(nombre_log+".txt","w")

        for j in range (len(ids)):
            log.write("Artículo " + str(j+1) + ":\n" + "ID del ítem:\t\t\t" + str(ids[j])+"\n" + "Título del ítem:\t\t" +str(titles[j])+ "\n" + "ID de la catgoría del ítem:\t" + str(category_ids[j]+ "\n" + "Nombre de la categoría:\t\t" +str(domain_ids[j])+"\n\n"))
        log.close()
        print("Se ha creado el archivo " + nombre_log + ".txt\n")
        print()

if __name__ == "__main__":
    print("\nBIENVENIDO/A ESTE PROGRAMA GENERA UN LOG CON LAS PUBLICACIONES DE UN USUARIO DE MERCADO LIBRE DANDO EL ID DE DICHO USUARIO:\n")
    
    app_id = input("Ingrese la ID de la app: ")
    app_id = app_id.strip()
    cli_secret = input("Ingrese el client sectret de la app: ")
    cli_secret = cli_secret.strip()
    redirect_uri = input("Ingrese la URL de redirección URI de la app: ")
    redirect_uri = redirect_uri.strip()
    
    sellers = []

    cant_revisar = int(input("Ingrese la cantidad de sellers a revisar: "))

    for i in range (cant_revisar):
        print()
        seller_id = input("Ingrese el Nro ID del seller (ej: 179571326 / 114457637): ")
        sellers.append(seller_id)
    
    print("\nSellers IDs a revisar: " + str(sellers))
    
    for j in range (cant_revisar):
        token = generar_token(app_id, cli_secret, redirect_uri)
        crear_log(token, sellers[j])
