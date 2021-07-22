# Ejercicio - Investigación / Script
Ejercicio de script para el Test Gestión Operativa - Básico

El script permite generar un archivo con las publicaciones de un vendedor de Mercado Libre Argentina sabiendo su selled_id, en caso de no conocerlo puede usarse el siguiente script para obtenerlo "https://github.com/GCE140/obtener_id_usuario_MELI".

El programa funciona de acuerdo a lo especificado en "https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas#Trabajar-con-Scan-Hash", para lo cual debe generarse un token asociado a una app de Mercado Libre, esto puede hacerse siguiendo las instrucciones en "https://developers.mercadolibre.com.ar/es_ar/mi-primera-aplicacion#Crea-una-aplicacion-en-Mercado-Libre", en este caso se usó como redirect_uri a https://mercadolibre.com.ar.

Una vez creada la app se obtiene el App ID y el Client Secret, con ellos se pedirá un código de autenticación a "https://auth.mercadolibre.com.ar/authorization?response_type=code&client_id=(AQUI_VA_EL_APP_ID)&redirect_uri=https://mercadolibre.com.ar", esta direción devolverá por URL un código de autenticación, por ejemplo: "https://www.mercadolibre.com.ar/?code=TG-60f99e899a0da10008938bd7-47678875", en este caso el código es "TG-60f99e899a0da10008938bd7-47678875".

El programa utiliza el App ID, el Client Secret y el Código generado para consultar la API de Mercado Libre y generar un token de acuerdo a lo especificado en "https://developers.mercadolibre.com.ar/es_ar/autenticacion-y-autorizacion#Enviar-access-token-por-header".

Con el token conseguido se consulta la API que permite generar más de 1000 consultas, de acuerdo a lo explicado en "https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas#Trabajar-con-Scan-Hash".

Los resultados se guardan en un archivo de texto en la misma localización donde se encuentre el script contando el mismo con el siguiente formato: Artículo x: ID del ítem: MLAXXXXXXXXX Título del ítem: XXXXXXXXXXXXXXXXXX ID de la catgoría del ítem: MLAXXXXXX Nombre de la categoría: MLA-XXXXXXXXXXXX

La respuesta obtenida de la API es en formato json por lo que para trabajar con la misma es necesario el modulo json y el módulo requests ("pip install requests") a fin de poder enviar el GET a la url de la API.
