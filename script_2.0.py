import requests, json
from requests.api import request
from requests.exceptions import HTTPError
from requests.structures import CaseInsensitiveDict
from datetime import datetime

ahora = datetime.now()
formato_fecha = "%d-%m-%Y-%Hh-%Mm-%Ss"
texto_fecha = ahora.strftime(formato_fecha)

def generar_token(app_id, cli_secret):
    
    code = input("Ingrese el códigod de autenticación: ")
    code = code.strip()

    url = "https://api.mercadolibre.com/oauth/token"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["content-type"] = "application/x-www-form-urlencoded"

    data = f"grant_type=authorization_code&client_id={app_id}&client_secret={cli_secret}&code={code}&redirect_uri=https://mercadolibre.com.ar"

    resp = requests.post(url, headers=headers, data=data)

    json_data = json.loads(resp.text)

    print("Reporte de status: " + str(resp.status_code))
    print("El token es:\t" + json_data["access_token"])
    return json_data["access_token"]


def crear_log(token, seller_id):

    url = f"https://api.mercadolibre.com/users/{seller_id}/items/search?search_type=scan"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url, headers=headers)

    print("Reporte de status: " + str(resp.status_code))

    if resp.status_code != 200:
        print("Error de acceso al servicio.")
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
        print("Se ha creado el archivo " + nombre_log + ".txt")
        print()

if __name__ == "__main__":
    print("\nBIENVENIDO/A ESTE PROGRAMA GENERA UN LOG CON LAS PUBLICACIONES DE UN USUARIO DE MERCADO LIBRE DANDO EL ID DE DICHO USUARIO:\n")
    
    app_id = input("Ingrese la ID de la app: ")
    app_id = app_id.strip()
    cli_secret = input("Ingrese el client sectret de la app: ")
    cli_secret = cli_secret.strip()

    sellers = []

    cant_revisar = int(input("Ingrese la cantidad de sellers a revisar: "))

    for i in range (cant_revisar):
        print()
        seller_id = input("Ingrese el Nro ID del seller (ej: 179571326 / 114457637): ")
        sellers.append(seller_id)
    
    print("\nSellers IDs a revisar: " + str(sellers) + "\n")
    
    for j in range (cant_revisar):
        token = generar_token(app_id, cli_secret)
        crear_log(token, sellers[j])