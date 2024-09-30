# Weather_API_python

Tento Python skript získává aktuální údaje o počasí pro zadané město pomocí OpenWeatherMap API.

# Popis
Tento projekt umožňuje uživatelům zadat název města a získat aktuální informace o počasí (hlavní popis počasí a viditelnost). Pokud město nelze najít, uživateli se zobrazí odpovídající chybová zpráva.

# Funkce
Získává aktuální údaje o počasí pomocí OpenWeatherMap API.
Zobrazuje hlavní popis počasí (např. "Clear", "Cloudy").
Poskytuje podrobný popis počasí (např. "Clear sky").
Umožňuje elegantní zpracování neplatných nebo neexistujících názvů měst, zobrazením chybové zprávy ("No city found").

# Požadavky
Python 
Modul requests pro odesílání HTTP požadavků

# Jak používat
Získejte API key: 
Zaregistrujte se na OpenWeatherMap, abyste získali API key zdarma.
Nahraďte proměnnou api_key ve skriptu vlastním API klíčem.
Použitý API key z OpenWeatherMap: https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}
London - nahrazen inputem {City}

# Příklad
Enter city: Praha
Current weather in Praha is Clear.
Current visibility in Praha is clear sky.

Pokud město nelze najít:
Enter city: Gdfgadg
No city found. Please check the city name and try again.
