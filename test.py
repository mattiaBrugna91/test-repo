import numpy as np

lista_random = np.random.rand(10)

print(lista_random)

# COMANDI UNIX operazioni da terminale per muovarmi sulle cartelle: 
# ls = lista cartelle e file presenti 
# cd <nome cartella> = cambio cartella 
# pwd = ci spiega dove siamo <path> 
# python test.py = testa codice 
# git init = creo repository git 
# ls -alh , ls .git= visualizzo file descrittivi della storia e della comunicazione con il server remoto 
# git status = situazione repository git 
# add test.py = aggiungo il file in un area locale in attesa di fare il commit, diventa tracked 
# git commit -m "primo commit di test.py" 

# git config --global user.email "brugnaromattia91@gmail.com" 
# git config --global user.name "Mattia"                      = per impostare le mie credenziali se non prende il commit

# git remote add test.py <url> -- url repository creata su github

# git remote add origin https://github.com/mattiaBrugna91/test-repo.git
# git branch -M main
# git push -u origin main                                                = per inserire il fil creato in locale nella repository remota 
# git pull per scaricare tutto in locale e creare un ramo di sviluppo in cui applicare dei cambiamenti