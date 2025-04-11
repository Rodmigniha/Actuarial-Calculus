import streamlit as st
from utils import commut
import io
import pandas as pd
import numpy as np

page = st.sidebar.selectbox('Navigation', ["Accueil", "Calcul des commutations"])

if page == "Accueil":
    st.title("🧮 Application de calcul actuariel : commutations sur tables de mortalité")
    st.markdown("""
    ### 🧾 Description de l’application

    Cette application interactive permet d’importer une **table de mortalité** au format Excel 
    et de calculer automatiquement les **nombres de commutation** et d'autres calculs fondamentaux utilisés en mathématiques actuarielles.

    Grâce à une interface simple et intuitive, l’utilisateur peut :

    - 📂 **Téléverser** une table de mortalité personnalisée ;
    - 🔢 **Sélectionner** dynamiquement les colonnes correspondant à l’âge et aux effectifs survivants (`lx`) ;
    - 📉 **Définir un taux d’intérêt technique** personnalisé ;
    - 🧮 **Visualiser instantanément** les colonnes de commutation calculées ;
    - 💾 **Téléchargement de la table enrichie** au format Excel
    """)
    t = st.selectbox("Voir les formules ?",["formules cachées","Afficher les formules"])
    if t == "Afficher les formules" :
    
        st.latex(r"d_x = l_x - l_{x+1}")
        st.latex(r" C_x = d_x \times v^{x+1/2}")
        st.latex(r" D_x = l_x \cdot v^x") 
        st.latex(r"N_x = \sum_{k=x}^{\omega} D_k")
        st.latex(r" S_x = \sum_{k=x}^{\omega} N_k")
        st.latex(r" M_x = \sum_{k=x}^{\omega} C_k")
        st.latex(r" R_x = \sum_{k=x}^{\omega} M_k")

    st.markdown("""
    ### 🎯 Objectif

    L’objectif est de **faciliter l’analyse actuarielle** de tables de mortalité et 
    de **rendre accessible** le calcul des commutations pour les professionnels de l’assurance vie.
    """)


elif page == "Calcul des commutations":
    st.title("🧮 Calcul des commutations")
    
    st.markdown("Vous n'avez pas de table de mortalité ?")
    st.markdown("➡️ Téléchargez un modèle prêt à remplir ci-dessous 👇")
    
    with open('template_tabl_mortalite.xlsx', "rb") as f:
        bytes_data = f.read()

        st.download_button(
            label="📥 Télécharger le template Excel",
            data=bytes_data,
            file_name="template_table_mortalite.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    tabl_mort = st.file_uploader('Veuillez téléverser le fichier Excel de table de mortalité', type='xlsx')

    if tabl_mort is not None:
        data = pd.read_excel(tabl_mort)
        st.write("Aperçu des données :", data.head(3))
        
        age = st.sidebar.selectbox('Choisissez la colonne des âges', data.columns, index=0)
        if not np.issubdtype(data[age].dtype, np.number):
            st.error("La colonne sélectionnée pour l'âge doit contenir uniquement des nombres.")
    
        l = st.sidebar.selectbox('Choisissez la colonne des Lx', data.columns, index=1)
        if not np.issubdtype(data[l].dtype, np.number):
            st.error("La colonne sélectionnée pour lx doit contenir uniquement des nombres.")
        i = float(st.sidebar.text_input('Entrez le taux intérêt technique', 0.035))
        calc = st.sidebar.selectbox('Ajouter un calcul actuariel', 
                                    ['non', "Term immediate annuity", 
                                     "Differed annuity", 
                                     "Term insurance - yearly", 
                                     "Pure endowment","Endowment insurance - yearly"])
        n = 1
        if calc != 'non':
            n = int(st.sidebar.text_input('Entrez le différé en année', 1))

        if i is not None:
            tabl = commut(data, age, l, i, n, type=calc)
            st.write("Table enrichie avec les commutations :")
            st.dataframe(tabl)
            
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                tabl.to_excel(excel_writer=writer, index=False, sheet_name='Commutations')
                
            buffer.seek(0)    
            st.download_button(
                label="📥 Télécharger la table enrichie au format Excel",
                data=buffer.getvalue(),
                file_name="table_commutations.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
