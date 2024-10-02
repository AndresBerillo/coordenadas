from geopy.geocoders import Nominatim

# Crear un geolocalizador
geolocator = Nominatim(user_agent="geoapiExercises")

# Lista de direcciones
direcciones = [
    "Av. Corrientes 2039, Buenos Aires",
    "Libertad 655, Buenos Aires"
]

# Función para obtener coordenadas
def obtener_coordenadas(direcciones):
    coordenadas = {}
    for direccion in direcciones:
        location = geolocator.geocode(direccion)
        if location:
            coordenadas[direccion] = (location.latitude, location.longitude)
        else:
            coordenadas[direccion] = None
    return coordenadas

# Obtener y mostrar las coordenadas
coordenadas = obtener_coordenadas(direcciones)
for direccion, coords in coordenadas.items():
    if coords:
        print(f"{direccion}: {coords}")
    else:
        print(f"{direccion}: No se encontraron coordenadas.")
