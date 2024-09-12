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
        
        # Ottieni i post del profilo
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

# Input per inserire i nomi utenti separati da virgola
usernames_input = st.text_input('Inserisci gli username di Instagram separati da virgola:')

# Bottone per eseguire il controllo
if st.button('Controlla'):
    if usernames_input:
        # Split degli username separati da virgola
        usernames = [username.strip() for username in usernames_input.split(',')]
        
        results = []
        for username in usernames:
            result = get_last_post_date(username)
            results.append(result)
        
        # Visualizza i risultati
        for result in results:
            st.write(result)
    else:
        st.write("Per favore, inserisci almeno un nome utente.")
