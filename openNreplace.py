f = open('/Users/samos/Desktop/x.txt', 'rw')
data = f.read().replace(' https://', str('\n')+'https://')
print(data)
f.close()