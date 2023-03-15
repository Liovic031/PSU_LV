radni_sati = int(input('Unesi broj radnih sati:'))
satnica = float(input('Unesi satnicu:'))

def total_euro(x, y):
    z = x * y
    return z

print('Vasa placa iznosi ', total_euro(radni_sati, satnica), ' eura.')