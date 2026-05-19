# 🚗 System Zarządzania Flotą Pojazdów

Nowoczesna aplikacja webowa stworzona w frameworku **Django (Python)** oraz ostylowana za pomocą **Bootstrap 5**. System umożliwia pracownikom/kierowcom rezerwację pojazdów służbowych, a administratorom pełne zarządzanie dostępnością floty.

## ✨ Główne Funkcjonalności
* **Lista Pojazdów:** Dynamiczny podgląd wszystkich aut w bazie wraz z ich aktualnymi statusami operacyjnymi.
* **System Rezerwacji:** Możliwość rezerwacji wybranego auta na konkretny przedział czasowy.
* **Zaawansowana Walidacja (Logika Biznesowa):**
  * Blokada rezerwacji dat w przeszłości.
  * Blokada ustawienia końca rezerwacji przed jej rozpoczęciem.
  * **Algorytm anty-konfliktowy:** System uniemożliwia rezerwację auta w terminie, który nakłada się na inną, istniejącą rezerwację.
* **Automatyzacja Statusów:** Po udanej rezerwacji, auto automatycznie zmienia status na `Zarezerwowany`.
* **Dashboard Kierowcy:** Dedykowany widok dla zalogowanego użytkownika z listą jego nadchodzących wyjazdów.
* **Dashboard Managera:** Panel dla administratora pokazujący całą flotę w formie czytelnej, kolorowej tabeli statusów.

## 🛠️ Technologie
* **Backend:** Python 3.14+ / Django 6.0+
* **Frontend:** HTML5, CSS3, Bootstrap 5, Django-Bootstrap5
* **Baza danych:** SQLite (wbudowana)

## 🚀 Jak uruchomić projekt lokalnie?

1. Sklonuj repozytorium:
  
   git clone [https://github.com/Antonia232/Projekt-System-Zarz-dzania-Flot-Pojazd-w-.git](https://github.com/Antonia232/Projekt-System-Zarz-dzania-Flot-Pojazd-w-.git)
