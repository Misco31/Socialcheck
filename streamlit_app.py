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
        
        # Ottieni la data del post più recente (il primo nella lista dei post)
        last_post = next(posts)
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
