import socket

indirizzo_ip = input('Inserisci indirizzo ip: ')
porte = input('Inserire un renge di porte: ')

minporta = int(porte.split('-')[0])
massporta = int(porte.split('-')[1])+1


print('Scansione ip: ', indirizzo_ip, 'Dalla porta', minporta, 'alla porta',massporta)

for port in range(minporta, massporta ):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	status = sock.connect_ex((indirizzo_ip, port))
	if(status == 0):
		print('<<< Port',port,'- OPEN >>>',)
	
	sock.close()