import instaloader
import streamlit as st

# Funzione per ottenere la data dell'ultimo post
def get_last_post_date(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        posts = profile.get_posts()
        last_post = next(posts)
        return f"L'ultimo post di {username} è stato pubblicato il {last_post.date}"
    except Exception as e:
        return f"Errore nel recupero delle informazioni per {username}: {e}"

# Creazione dell'interfaccia con Streamlit
st.title('Controlla gli ultimi post su Instagram')

# Input per inserire il nome utente
username = st.text_input('Inserisci un username di Instagram:')

# Bottone per eseguire il controllo
if st.button('Controlla'):
    if username:
        result = get_last_post_date(username)
        st.write(result)
    else:
        st.write("Per favore, inserisci un nome utente valido.")
