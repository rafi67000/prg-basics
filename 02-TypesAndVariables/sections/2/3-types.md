# Przewidywane 
```
50 Int
149.17 Float 
4 * 7 Int
4.0 * 7 Float
"Krakow University of Economics" String
True Boolean
2 > 5 Boolean
```

# Wynik
`cat 3-input | xargs -d '\n' -I {} python3 -c "print('''{}:''', type({}).__name__)"`
```python
print('''50:''', type(50).__name__)
print('''149.17:''', type(149.17).__name__)
print('''4 * 7:''', type(4 * 7).__name__)
print('''4.0 * 7:''', type(4.0 * 7).__name__)
print('''"Krakow University of Economics":''', type("Krakow University of Economics").__name__)
print('''True:''', type(True).__name__)
print('''2 > 5:''', type(2 > 5).__name__)
```
```
50: int
149.17: float
4 * 7: int
4.0 * 7: float
"Krakow University of Economics": str
True: bool
2 > 5: bool
```