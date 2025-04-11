# 🧮 Actuarial-Calculus

**Actuarial-Calculus** est une application web interactive permettant de calculer automatiquement les **nombres de commutation** à partir d’une table de mortalité. Elle s’adresse aux **actuaires** ou tout professionnel ayant besoin de manipuler des tables de mortalité pour des calculs d’assurance vie.

## 🚀 Fonctionnalités

- 📂 Import d’une **table de mortalité Excel** ;
- 🔢 Sélection dynamique des colonnes `âge` et `lₓ` ;
- 🧮 Calcul automatique des nombres de commutation :  
  `dₓ`, `Cₓ`, `Dₓ`, `Nₓ`, `Mₓ`, `Sₓ`, `Rₓ`, `äₓ`, `Aₓ`, `aₓ`, etc.
- ➕ Calculs actuariels supplémentaires :
  - Rente temporaire (`äₓ:n`)
  - Rente différée (`n|äₓ`)
  - Assurance temporaire décès (`Aₓ:n`)
  - Assurance en cas de vie pure (`nEₓ`)
  - Assurance mixte (`Aₓ:n_mixte`)
- 📊 Affichage instantané des résultats ;
- 💾 Téléchargement de la table enrichie au format Excel ;
- 📖 Affichage optionnel des **formules mathématiques**.

---

## 🖥️ Interface utilisateur

L’interface est divisée en deux onglets :
- **Accueil** : présentation de l’application et rappel des formules.
- **Calcul des commutations** : chargement de la table, sélection des paramètres et obtention des résultats.

---

## 📸 Aperçu de l’application

![screenshot](https://github.com/Rodmigniha/Actuarial-Calculus/blob/main/data/Capture01.PNG)
![screenshot](https://github.com/Rodmigniha/Actuarial-Calculus/blob/main/data/Capture02.PNG) 
![screenshot](https://github.com/Rodmigniha/Actuarial-Calculus/blob/main/data/Capture03.PNG)

---

## 🧰 Prérequis

- Python >= 3.9
- Packages :
  - `streamlit`
  - `pandas`
  - `numpy`
  - `openpyxl`
  - `pyarrow`
  - `xlsxwriter`

## Installation

###  Cloner le repository

```bash
git clone https://github.com/Rodmigniha/Actuarial-Calculus.git
cd Actuarial-Calculus
```
## Installation des dépendances :
```bash
pip install -r requirements.txt
```
## ⚙️ Lancer l'application

```bash
streamlit run main.py
```
## 📁 Structure du projet
```bash
Actuarial-Calculus/
│
├── main.py               # Application principale Streamlit
├── utils.py              # Fonctions de calcul des commutations
├── requirements.txt      # Dépendances Python
├── data/
│   └── Capture.png    # Capture d’écran de l’application en marche
│   └── Capture.png    # Capture d’écran de l’application en marche
│   └── template_tabl_mortalite.xlsx # modèle de table de mortalité
└── README.md             
```
## Contribution

Les contributions sont les bienvenues ! Veuillez suivre ces étapes :

1. Forkez le projet
2. Créez une branche (`feature-nouvelle-fonctionnalite`)
3. Faites vos modifications et committez (`git commit -m "Ajout d'une nouvelle fonctionnalité"`)
4. Poussez la branche et ouvrez une pull request

## Auteurs

- **Rodrigue MIGNIHA** 

📧 Contacts : kidam.migniha@gmail.com