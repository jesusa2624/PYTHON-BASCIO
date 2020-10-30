# and para comparar si dos valores son verdaderos.
# or para comparar si dos valores son falsos.
# not para invertir el valor booleano.
# == Compara dos valores y te dice si son iguales o no.
# != Compara dos valores y te dice sin son diferentes o no.
# > Compara si es mayor que otro valor.
# > Compara si es menor que otro valor.
# >= igual o mayor que el valor a comparar.
# <= igual o menor que el valor a comparar.

es_estudiante = True
>>> es_estudiante
True
>>> trabaja = Falsa
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Falsa' is not defined
>>> trabaja = False
>>> trabaja
False
>>> es_estudiante and trabaja
False
>>> es_estudiante or trabaja
True
>>> not es_estudiante
False
>>> not trabaja
True
>>> numero1 = 5
>>> numero2 = 5
>>> numero1
5
>>> numero2
5
>>> numero1 == numero2
True
>>> numero3 = 7
>>> numero1 == numero3
False
>>> numero1 != numero3
True
>>> numero1 > numero3
False
>>> numero1 >= numero3
False