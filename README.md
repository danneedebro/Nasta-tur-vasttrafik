# Nästa-tur-vasttrafik
Hämtar nästa avgångar från en viss hållplats med hjälp av Västtrafiks API Reseplaneraren v2 på enklaste sätt

# Kräver bibliotek
- Requests
- base64
- datetime

# Instruktioner
1. Registrera en användare på https://developer.vasttrafik.se/portal/#/
2. Skapa en applikation under **"Mina applikationer"**
3. Låt den applikationen prenumerera på API:et **"Reseplaneraren v2"**
4. Under **"Mina applikationer"** välj aktuell applikation och kopiera tokens med beteckning *Nyckel* och *Hemlighet* och lägg in i koden 

# Vad gör koden
Västtrafik använder auktoriseringprotokollet [OAuth2](https://en.wikipedia.org/wiki/OAuth) som tillsammans med hjälp av två fasta tokens (*Nyckel/Key* och *Hemlighet/Secret*) genererar en tillfällig accesstokens som skickas med i efterföljande GET-requests.

**Steg 1.** POST-request till https://api.vasttrafik.se/token med *KEY* och *SECRET* i headern (base64-kodade med kolon emellan). Det ger ett svar enligt

![Alt text](/pics/Pic1.png?raw=true "Optional Title")

**Steg 2.** GET-request till https://api.vasttrafik.se/bin/rest.exe/v2/location.name  för att hitta hållplats-ID för en hållplats given som en sträng

![Alt text](/pics/Pic2.png?raw=true "Optional Title")

**Steg 3.** GET-request till https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard  för att med hjälp av hållplats-ID hitta nästa avgångar

![Alt text](/pics/Pic3.png?raw=true "Optional Title")
