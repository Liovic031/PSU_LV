try:
    broj = float(input('Unesi broj u intervalu [0.0, 1.0]: '))
except:
    print('Pogresan unos!')

if broj >= 0.0 and broj < 0.6:
    print('F')
elif broj >= 0.6 and broj < 0.7:
    print('D')
elif broj >= 0.7 and broj < 0.8:
    print('C')
elif broj >= 0.8 and broj < 0.9:
    print('B')
elif broj >= 0.9 and broj <= 1.0:
    print('A')
else:
    print('Broj nije u zadanom intervalu!')