import streamlit as st
import random

st.set_page_config(page_title="Genética Mendeliana", layout="centered")

st.title("🧬 Práctica de Genética Mendeliana")

# Tipos de ejercicios disponibles
cruzamientos = [
    ("Aa", "Aa"),
    ("AA", "aa"),
    ("Aa", "aa"),
    ("AA", "Aa"),
    ("aa", "Aa"),
]

def generar_ejercicio():
    padre1, padre2 = random.choice(cruzamientos)
    genotipos = obtener_genotipos(padre1, padre2)
    genotipos_dict = {
        "AA": genotipos.count("AA"),
        "Aa": genotipos.count("Aa"),
        "aa": genotipos.count("aa")
    }
    return padre1, padre2, genotipos_dict

def obtener_genotipos(p1, p2):
    # cruza genética entre dos padres
    alelos1 = list(p1)
    alelos2 = list(p2)
    resultados = []
    for a1 in alelos1:
        for a2 in alelos2:
            genotipo = ''.join(sorted(a1 + a2))
            resultados.append(genotipo)
    return resultados

if "padre1" not in st.session_state:
    st.session_state.padre1, st.session_state.padre2, st.session_state.respuesta_correcta = generar_ejercicio()
    st.session_state.mostrado_feedback = False
    st.session_state.correcto = False

def verificar_respuesta(user_AA, user_Aa, user_aa):
    rc = st.session_state.respuesta_correcta
    try:
        ua, ub, uc = int(user_AA), int(user_Aa), int(user_aa)
        correcto = (ua == rc["AA"] and ub == rc["Aa"] and uc == rc["aa"])
        st.session_state.correcto = correcto
        st.session_state.mostrado_feedback = True
    except:
        st.session_state.correcto = False
        st.session_state.mostrado_feedback = True

def nuevo_ejercicio():
    st.session_state.padre1, st.session_state.padre2, st.session_state.respuesta_correcta = generar_ejercicio()
    st.session_state.mostrado_feedback = False
    st.session_state.correcto = False
    st.experimental_rerun()

# Mostrar ejercicio
st.subheader("Ejercicio:")
st.markdown(f"¿Cuál es la proporción genotípica del cruzamiento entre **{st.session_state.padre1} × {st.session_state.padre2}**?")
st.markdown("Ingresa la cantidad de descendientes esperados (en 4 total):")

col1, col2, col3 = st.columns(3)
with col1:
    user_AA = st.text_input("AA", value="0", key="input_AA")
with col2:
    user_Aa = st.text_input("Aa", value="0", key="input_Aa")
with col3:
    user_aa = st.text_input("aa", value="0", key="input_aa")

if st.button("Verificar respuesta"):
    verificar_respuesta(user_AA, user_Aa, user_aa)

if st.session_state.mostrado_feedback:
    if st.session_state.correcto:
        st.success("✅ ¡Correcto!")
    else:
        st.error("❌ Incorrecto.")
        rc = st.session_state.respuesta_correcta
        st.markdown(f"**Respuesta correcta:** AA: {rc['AA']}, Aa: {rc['Aa']}, aa: {rc['aa']}")

if st.button("Nuevo ejercicio"):
    nuevo_ejercicio()
