# Ejercicio - Investigación / Script
Ejercicio de script para el Test Gestión Operativa - Básico

El script permite generar un archivo con las publicaciones de un vendedor de Mercado Libre Argentina sabiendo su selled_id, en caso de no conocerlo puede usarse el siguiente script para obtenerlo "https://github.com/GCE140/obtener_id_usuario_MELI".




Los resultados se guardan en un archivo de texto en la misma localización donde se encuentre el script contando el mismo con el siguiente formato: Artículo x: ID del ítem: MLAXXXXXXXXX Título del ítem: XXXXXXXXXXXXXXXXXX ID de la catgoría del ítem: MLAXXXXXX Nombre de la categoría: MLA-XXXXXXXXXXXX

La respuesta obtenida de la API es en formato json por lo que para trabajar con la misma es necesario el modulo json y el módulo requests ("pip install requests") a fin de poder enviar el GET a la url de la API.
