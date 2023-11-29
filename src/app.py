
import streamlit as st

def buscar_jugador_similar(nombre, posicion, edad, habilidad):
    # Aquí podrías tener una lógica más avanzada basada en tus criterios de búsqueda
    # En este ejemplo, simplemente se devuelve un nombre aleatorio
    nombres_similares = ["Messi", "Ronaldo", "Neymar", "Mbappé"]
    return nombres_similares
def main():
    st.title("Buscador de Jugadores de Fútbol Similares")
    # Formulario para ingresar los criterios de búsqueda
    nombre = st.text_input("Nombre del Jugador:")
    posicion = st.selectbox("Posición:", ["Delantero", "Centrocampista", "Defensa", "Portero"])
    edad = st.slider("Edad:", min_value=18, max_value=40, value=25)
    habilidad = st.slider("Habilidad (1-100):", min_value=1, max_value=100, value=50)
    # Botón para realizar la búsqueda
    if st.button("Buscar Jugador Similar"):
        jugadores_similares = buscar_jugador_similar(nombre, posicion, edad, habilidad)
        if jugadores_similares:
            st.success(f"Jugadores similares a {nombre}: {', '.join(jugadores_similares)}")
        else:
            st.warning("No se encontraron jugadores similares.")
if __name__ == "__main__":
    main()
