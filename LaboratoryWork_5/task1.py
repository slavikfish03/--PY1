import pprint
pprint.pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
               for i in range(16)])  #перенос строки для читабельности
