# Weather_API_python

Tento Python skript získává aktuální údaje o počasí pro zadané město pomocí OpenWeatherMap API.

# Popis
Tento projekt umožňuje uživatelům zadat název města a získat aktuální informace o počasí (hlavní popis počasí a viditelnost). Pokud město nelze najít, uživateli se zobrazí odpovídající chybová zpráva.

# Funkce
Získává aktuální údaje o počasí pomocí OpenWeatherMap API.
Zobrazuje hlavní popis počasí (např. "Clear", "Cloudy").
Poskytuje podrobný popis počasí (např. "jasná obloha").
Umožňuje elegantní zpracování neplatných nebo neexistujících názvů měst, zobrazením chybové zprávy ("Město nenalezeno").

# Požadavky
Python 
Modul requests pro odesílání HTTP požadavků

# Jak používat
Získejte API klíč:
Zaregistrujte se na OpenWeatherMap, abyste získali API klíč zdarma.
Nahraďte proměnnou api_key ve skriptu vlastním API klíčem.


# Příklad
Enter city: Praha
Current weather in Praha is Clear.
Current visibility in Praha is clear sky.

Pokud město nelze najít:
Enter city: Gdfgadg
No city found. Please check the city name and try again.
