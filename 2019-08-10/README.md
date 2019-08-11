# Zadania

## Zadanie 1 - rozgrzewka

Utwórz funkcję, która zwróci sumę dwóch lub więcej argumentów

## Zadanie 2 - rozgrzewka

Utwórz funkcję, która zwróci resztę z dzielenia dwóch liczb.

## Zadanie 3 - rozgrzewka

Na swojej farmie masz kurczaki (dwie nogi), krowy (cztery nogi) i świnie (cztery nogi).
Napisz funkcję, która przyjmuje 3 argumenty: ilość kurczaków, ilość krów i ilość świń. Funkcja powinna zwrócić całkowitą sumę nóg na farmie.

## Zadanie 4 - rozgrzewka

Napisz funkcję rekurencyjną, która liczy silnię.

## Zadanie 5 - rozgrzewka

Napisz funkcję, która zwraca kod ASCII lub UTF-8 przekazanego znaku.
Przykład: `ctoa("A") ➞ 65`

## Zadanie 6 - rozgrzewka

Napisz funkcję, która liczy ilość wystąpień danego znaku.
Przykład: `numofchar(‘h’, ‘hello’) ➞ 1`

## Zadanie 7 - rozgrzewka

Napisz funkcję, która policzy, czy jest możliwe równe podzielenie pokrojonego ciasta pomiędzy osoby w pokoju.

`equal_slices(total_slices, number_of_recipients, slices_each)`

Przykład: `equal_slices(11, 5, 2) ➞ True`

## Zadanie 8 - rozgrzewka

Napisz funkcję, która wykryje, czy słowo jest palindromem.

Przykłady: https://pl.wikipedia.org/wiki/Palindrom#Polski

`is_palindrome('racecar')  ===  true`

## Zadanie 9 - rozgrzewka

FizzBuzz!
Napisz funkcję, która wypisze w konsoli:
* Cyfry od 1 do n
* “Fizz”, jeśli cyfra jest podzielne przez 3
* “Buzz”, jeśli cyfra jest podzielne przez 5
* “FizzBuzz”, jeśli cyfra jest podzielne przez 3 i 5

Przykład:

```
fizzBuzz(5)
1
2
fizz
4
buzz
```

## Zadanie 10 - rozgrzewka, ostatnia krew

Napisz funkcję, która sprawdzi, czy dwa podane słowa są anagramem.
Anagram oznacza wyraz, wyrażenie lub całe zdanie powstałe przez przestawienie liter bądź sylab innego wyrazu lub zdania, wykorzystujące wszystkie litery (głoski bądź sylaby) materiału wyjściowego.

Przykład: `anagram('finder', 'Friend')  --> true`

## Zadanie 10A - serio ostatnia krew

Fibonacci!

Napisz funkcję, która znajdzie i wypisze na ekranie N-tą cyfrę w ciągu Fibonacciego.

Ciąg Fibonacciego to ciąg liczb, którego kolejny element jest sumą dwóch poprzednich.

Dziesięć pierwszych liczb w ciągu: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Przykład: `fibonacci(3)  --> 2`

## Zadanie 11 - wzory matematyczne

Napisz funkcję, która będzie sprawdzać poprawność zapisu wzoru matematycznego.

Dopuszczalne znaki: `^()[]{}*+=-`

Przykład: `2 * (y^{(x + 2) * 6})`

Wynik: `True`

## Zadanie 12

Napisz aplikację pokazującą informacje o ruchu Międzynarodowej Stacji Kosmicznej (ISS)

Wykorzystaj dane udostępniane przez API: [https://open-notify.org/Open-Notify-API/ISS-Location-Now/](https://open-notify.org/Open-Notify-API/ISS-Location-Now/)

Przedstaw użytkownikowi następujące dane:
* prędkość ISS na podstawie dwóch odczytów
* droga przebyta przez ISS od początku zapisanych odczytów

