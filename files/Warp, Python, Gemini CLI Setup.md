
# Vodič za postavljanje okruženja: Warp, Python, `uv` i Gemini CLI

Ovaj vodič će vas detaljno provesti kroz postavljanje kompletnog razvojnog okruženja na Windows sistemu za Python projekte. Koristit ćemo moderne alate kako bismo povećali produktivnost, a krajnji cilj je kreiranje jednostavnog AI chatbota koji se povezuje s Googleovim AI servisima i koristi njihove napredne jezičke modele.

## 1. Dio: Instalacija osnovnih alata

https://www.youtube.com/watch?v=RoR4XJw8wIc&pp=ygUJbGFuZ2NoYWlu

**1. Instalirajte Warp terminal:**
*   **Šta je Warp?** To je moderan terminal koji je pametniji i lakši za korištenje od standardnog Command Prompta. Ima integrisanu AI pomoć, pamti vaše komande i omogućava rad u više tabova.
*   Idite na zvaničnu [**Warp web-stranicu**](https://www.warp.dev/), preuzmite instalacioni program za Windows i pokrenite ga.
*   Tokom instalacije, možete odabrati opciju *„Skip login for now“* (Preskoči prijavu za sada).
*   **Preporuka:** Zakačite Warp na programsku traku (*taskbar*) radi lakšeg pristupa.
*   **Napomena:** Ukoliko koristite stariji laptop, može doći do problema s prikazom interfejsa (da ne možete kliknuti na dugmadi i da je sve pomjereno za 10tak pixela). U tom slučaju, probajte sakriti taskbar u postavkama Windowsa, tj. uključite opciju Auto hide taskbar.
**2. Instalirajte Python:**
*   **Šta je Python?** To je programski jezik u kojem ćemo pisati kod za našu aplikaciju.
*   Idite na zvaničnu [**Python stranicu za preuzimanje**](https://www.python.org/downloads/).
*   Odaberite jednu od novijih verzija, kao što je Python 3.12, i preuzmite **Windows Installer (64-bit)**.
*   Tokom instalacije, **OBAVEZNO označite polje na kojem piše *„Add Python.exe to PATH“***.
    *   **Zašto je ovo važno?** Ovaj korak omogućava da iz bilo kojeg foldera na računaru pokrenete Python komande direktno u Warp terminalu. Ako ovo preskočite, sistem neće znati gdje se Python nalazi.

**3. Instalirajte `uv` (menadžer Python paketa):**
*   **Šta je `uv`?** To je alat koji služi za instaliranje dodataka (paketa) za Python. Zamislite ga kao trgovinu aplikacija za vaš Python projekat. Izuzetno je brz i efikasan.
*   Otvorite svoj novoinstalirani **Warp terminal**.
*   Kopirajte i pokrenite sljedeću PowerShell komandu:
    ```powershell
    irm https://astral.sh/uv/install.ps1 | iex
    ```
*   Nakon instalacije, zatvorite i ponovo otvorite Warp. Provjerite da li je instalacija uspješna kucanjem komande `uv --version`.
*   `uv` zajedno sa `pip` (Package installer for Python) ima pristup hiljadama Python paketa koji se nalaze na stranici www.pypi.org

**4. Instalirajte Node.js:**
*   **Zašto nam treba Node.js?** Iako programiramo u Pythonu, alat Gemini CLI koji ćemo koristiti napravljen je pomoću Node.js tehnologije. Moramo ga instalirati da bi taj alat radio.
*   Idite na zvaničnu [**Node.js web-stranicu**](https://nodejs.org/) i preuzmite LTS (*Long-Term Support*) verziju.
*   Pokrenite instalacioni program i prođite kroz instalaciju prihvatajući zadane opcije.
*   Nakon instalacije, ponovo zatvorite i otvorite Warp. Provjerite instalaciju kucanjem komande `node --version`.

**5. Instalirajte Visual Studio Code (VS Code):**
*   **Šta je VS Code?** To je najpopularniji besplatni uređivač koda. U njemu ćemo pisati i pregledati naš Python kod.
*   Idite na [**zvaničnu stranicu za preuzimanje**](https://code.visualstudio.com/download) i pokrenite instalaciju.
*   Tokom instalacije, obavezno označite opcije **'Add "Open with Code" action to Windows Explorer file context menu'** i **'...directory context menu'**.
    *   **Zašto je ovo korisno?** Ovo će vam omogućiti da desnim klikom na bilo koji folder odmah otvorite taj projekat u VS Code-u.

## 2. Dio: Podešavanje Gemini CLI

**1. Instalirajte Gemini CLI:**
*   Otvorite Warp i pokrenite sljedeću `npm` (*Node Package Manager*) komandu kako biste globalno instalirali Google Gemini CLI:
    ```powershell
    npm install -g @google/gemini-cli
    ```
*   **Rješavanje problema:** Ako dobijete grešku u vezi sa pravilima o izvršavanju skripti (*script execution policies*), to je sigurnosna mjera Windowsa. Warp AI asistent vam može pomoći. Ukucajte `#` i pitajte ga na engleskom: `how to fix powershell script execution policy error`. On će vam ponuditi komandu (najčešće `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`) koju trebate pokrenuti.

**2. Preuzmite svoj Gemini API ključ:**
*   **Šta je API ključ?** To je vaša lična "lozinka" koja Google-u dokazuje da ste vi ovlašteni da koristite njihove AI modele.
*   Idite na [**Google AI Studio**](https://aistudio.google.com/app/apikey).
*   Kliknite na dugme *„Create API key in new project“*.
*   Kopirajte generisani ključ. **ČUVAJTE OVAJ KLJUČ!** Nemojte ga dijeliti javno jer on omogućava pristup vašem nalogu.

**3. Postavite API ključ:**
*   Da bi Gemini CLI znao koji je vaš ključ, morate ga sačuvati na računaru.

    **1. Metoda (Preporučeno za početnike): Trajna sistemska varijabla**
    *   U Warp-u koristite AI pomoć. Ukucajte `#`, a zatim unesite svoj upit (na engleskom):
        ```
        # Please set a persistent environment variable named GEMINI_API_KEY with the value [ZALIJEPITE_SVOJ_API_KLJUČ_OVDJE]
        ```
    *   Zamijenite `[ZALIJEPITE_SVOJ_API_KLJUČ_OVDJE]` sa ključem koji ste kopirali. Pokrenite komandu koju vam Warp ponudi.
    *   Zatvorite i ponovo otvorite Warp.
    *   Pokrenite komandu `gemini`. Kada vas pita kako se želite prijaviti, odaberite opciju **„Use the Gemini API key from the environment variable“**.

    **2. Metoda (Naprednija opcija): `.env` datoteka**
    *   Ova metoda čuva ključ unutar projektnog foldera. U folderu `MojGeminiChatbot` napravite novu datoteku i nazovite je `.env`. Unutar te datoteke napišite samo jedan red: `GEMINI_API_KEY="VAŠ_KLJUČ_IDE_OVDJE"` i sačuvajte. Gemini CLI će automatski prepoznati ovaj ključ kada ga pokrenete iz tog foldera.

## 3. Dio: Kreiranje prvog AI chatbot projekta

**1. Kreirajte folder projekta i virtuelno okruženje:**
*   Na radnoj površini (*Desktop*), kreirajte novi folder i nazovite ga `MojGeminiChatbot`.
*   Desni klik na folder i odaberite **Open in Warp**.
*   Unutar Warp terminala, kreirajte virtuelno okruženje komandom:
    ```powershell
    uv venv
    ```
    *   **Šta je virtuelno okruženje?** Zamislite ga kao zasebnu kutiju za svaki vaš projekat. Svi Python paketi koje instalirate za ovaj chatbot bit će smješteni u tu "kutiju" (`.venv` folder) i neće smetati drugim projektima na vašem računaru.
*   Aktivirajte ga komandom:
    ```powershell
    .venv\Scripts\activate
    ```
    Vidjet ćete `(.venv)` ispred komandne linije, što znači da je vaša "kutija" aktivna.

**2. Generišite kod za chatbot pomoću Gemini CLI:**
*   Sada ćemo reći Gemini-ju da napiše kod za nas. Koristimo detaljan upit (eng. *prompt*) na engleskom jeziku:
    ```powershell
    gemini "Create a simple chatbot application using Python and the Streamlit library. The application should have a user input field and display the conversation history. Use the 'gemini-1.5-flash-latest' model for the chat logic. Generate two files: 'app.py' for the application code and 'requirements.txt' listing the necessary packages (like streamlit and google-generativeai)."
    ```
*   Gemini će automatski kreirati datoteke `app.py` (glavni kod) i `requirements.txt` (spisak instaliranih Python paketa) u vašem folderu.

**3. Instalirajte potrebne zavisnosti (*dependencies*) uko**
*   **Šta je `requirements.txt`?** To je kao spisak za kupovinu. U njemu piše koje sve Python pakete (`streamlit`, `google-generativeai` itd.) treba instalirati da bi aplikacija radila.
*   Instalirajte sve sa spiska koristeći `uv`:
    ```powershell
    uv pip install -r requirements.txt
    ```

**4. Pokrenite svoju chatbot aplikaciju:**
*   Pokrenite Streamlit aplikaciju sljedećom komandom:
    ```powershell
    streamlit run app.py
    ```
*   Ova komanda će otvoriti novi tab u vašem browseru sa pokrenutim chatbotom. Sada možete komunicirati sa svojom prvom AI aplikacijom!

**5. Rješavanje problema: Update modela**
*   Ponekad, AI modeli zastarijevaju i Google objavljuje nove, bolje verzije. Ako dobijete grešku da model nije pronađen (*not found*), uradite sljedeće:
    1.  Otvorite datoteku `app.py` u **Visual Studio Code-u**.
    2.  Pronađite liniju koda gdje se spominje ime modela, npr. `model_name="gemini-pro"`.
    3.  Zamijenite staro ime sa nekim od novijih modela. Dobar izbor je `"gemini-1.5-flash-latest"` ili `"gemini-1.5-pro-latest"`. Kompletnu listu dostupnih modela možete naći na [zvaničnoj Google dokumentaciji](https://ai.google.dev/models/gemini).
    4.  Sačuvajte datoteku. Streamlit će automatski osvježiti aplikaciju u pregledniku.