import instaloader
import streamlit as st

# Funzione per ottenere la data dell'ultimo post senza cache
def get_last_post_date(username):
    L = instaloader.Instaloader()

    # Disabilitare la cache per ottenere sempre dati aggiornati
    L.download_pictures = False
    L.save_metadata = False
    L.post_metadata_txt_pattern = ""

    try:
        # Carica il profilo Instagram
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Forza l'aggiornamento del profilo
        posts = profile.get_posts()
        
        # Ottieni il primo post (il più recente)
        last_post = next(posts)
        
        # Formatta la data del post
        last_post_date = last_post.date
        return f"L'ultimo post di {username} è stato pubblicato il {last_post_date.strftime('%d %B %Y, %H:%M:%S')}"

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
