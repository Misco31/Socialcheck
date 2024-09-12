import instaloader
import streamlit as st

# Funzione per ottenere la data dell'ultimo post
def get_last_post_date(username):
    L = instaloader.Instaloader()
    try:
        # Carica il profilo Instagram
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Ottiene i post del profilo
        posts = profile.get_posts()
        
        # Ottieni la data dell'ultimo post
        last_post = next(posts)
        last_post_date = last_post.date
        
        return f"L'ultimo post di {username} è stato pubblicato il {last_post_date}"
    
    except Exception as e:
        return f"Errore nel recupero delle informazioni per {username}: {e}"

# Creazione dell'interfaccia Streamlit
st.title('Controlla gli ultimi post su Instagram')

# Input per inserire il nome utente Instagram
username = st.text_input('Inserisci un username di Instagram:')

# Bottone per eseguire la ricerca
if st.button('Controlla'):
    # Mostra il risultato
    result = get_last_post_date(username)
    st.write(result)
