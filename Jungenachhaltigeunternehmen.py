import streamlit as st
import pandas as pd
import altair as alt

st.header("Junge Menschen arbeiten lieber für nachhaltige Unternehmen")
st.subheader("Altersverteilung der Personen, die bevorzugen für Unternehmen arbeiten, die sich für Nachhaltigkeit einsetzen")

source = pd.DataFrame({
        'Anteil(%)': [9, 49, 26, 13, 3],
        'Altersgruppe': ['bis 20', '21-34', '35-49', '50-64', 'ab 65']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Altersgruppe:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    /
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Nielsen")