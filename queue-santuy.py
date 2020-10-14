#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque

antrian_cs = deque([])
no_urut_cs = 0

antrian_teller = deque([])
no_urut_teller = 0

def tampilkanDaftarAntri(data):
    for d in data:
        print(d)

while True:
    perintah = input('Tekan 1 untuk antrian CS, tekan 2 untuk antrian teller, tekan NOW untuk check antrian sekarang: \n')
    if perintah == '1':
        no_urut_cs += 1
        antrian_cs.append(no_urut_cs)
        print('Antrian ke: ' , no_urut_cs)
    elif perintah == '2':
        no_urut_teller += 1
        antrian_teller.append(no_urut_teller)
        print('Antrian ke: ' , no_urut_teller)
    elif perintah == 'OUT CS':
        print(antrian_cs.popleft())
    elif perintah == 'OUT TELLER':
        print(antrian_teller.popleft())
    elif perintah == 'NOW TELLER':
        print (antrian_teller)
    elif perintah == 'SHOW QUEUE CS':
        tampilkanDaftarAntri(antrian_cs)
    elif perintah == 'SHOW QUEUE TELLER':
        tampilkanDaftarAntri(antrian_teller)
    elif perintah == 'EXIT':
        break;
    else:
        print ('Perintah tidak diketahui')
