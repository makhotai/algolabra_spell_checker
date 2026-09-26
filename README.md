# README

## Runing the program

To run the program start the `app.py` file.

The program uses a smaller test dictionary by default. However, if you want to test the spell checker with a larger vocabulary (containing 10000+ Finnish words), you need to change following line in `src/services/spelchecker.py`, inside the `SpellChecker` class:

```python
def __init__(self, trie=None, path_wl=PATH_WL_TEST):
```

to:

```python
def __init__(self, trie=None, path_wl=PATH_WL):
```