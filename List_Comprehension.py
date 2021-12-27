"""QUESTION

Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u.

Sample Input
awesome

Sample Output
['w', 's', 'm']

ANSWER"""

word= input()
vowels= ["a","e","i","o","u"]

unsuz=[m for m in word if m not in vowels]
print(unsuz)
