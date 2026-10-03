# Weekly report 5
This week I mostly worked on the implementation document and did not implement much new functionality. I tried to keep `implementation.md` simple while also keeping the technical information precise and specific. I hope that I did not write too much. Writing the pseudocode left me confused (especially for the unrestricted Damerau-Levenshtein distance). I did not want to copy/paste a version from Wikipedia or use my own python code for that purpose, since it might look too complicated. I decided to experiment with both the free versions of ChatGPT-5 and Gemini and asked them to suggest easy-to-understand pseudocode based on my own code. The result did not really look like traditional pseudocode, but the logic and main operations were depicted correctly, so I used some of their output in my `implementation.md`.

The other aspect was peer review. I had to evaluate a scientific calculator program, also written in Python. It was interesting (yet challenging) to explore a very different topic and algorithm. As far as I understand, one of the main factors to consider when testing the program should be error notifications and strict input criteria, so that the program does not return incorrect outputs. So, it significantly differs from the spell-checker idea that I have been implementing. I found several bugs in the program's code, however, I really tried to emphasize the good parts of the project :)

I also attended a testing guidance session on Thursday in Kumpula. Unfortunately, I got so anxious that I could not even answer properly... However, the session was still beneficial and interesting, since I got to hear about other students' projects and the algorithms behind them.

Next week I would like to mostly polish my code and documentation.

## Questions for the course instructor

Last week I received feedback about testing that:
"Se, mitä olisi kiinnostavaa tutkia, olisi kuinka usein ohjelma osaa ehdottaa oikeaa sanaa väärin kirjoitetun tilalle. Ei kuitenkaan ole olemassa sopivaa dataa, jolla tätä voisi testata. Tarvittaisiin suuri määrä ihmisen kirjoittamaa tekstiä, johon sisältyisi tieto siitä mitkä sanat on kirjoitettu väärin, ja mitä sanaa käyttäjä on tarkoittanut."

I think that it significantly depends on the purpose of the program and the language being checked. For example, if we are talking about typing errors that can be caused by pressing the wrong key on the keyboard, that could mean that the algorithm could be optimized and tested in one way. On the other hand, if we want to correct just spelling mistakes (e.g. "aple" - "apple"), the optimization can be much more challenging.

Anyways, I understand that this course does not require such deep testing and optimization. However, I think that I could run some kind of test based on the suggestion above. Unfortunatelly, the (rather long) list of mistakes is only available in English. Maybe I could also test my program using an English word list and [this list of commonly misspelled words](https://en.wikipedia.org/wiki/Commonly_misspelled_English_words). Does that sound adequate and appropriate?

## Time spent

| date | time |
| ----- | ------------- |
| 30.9  | 3 h            |
| 1.10  | 4 h            |
| 2.10  | 1 h            |
| 3.10  | 2 h            |

**week total: 10 h**