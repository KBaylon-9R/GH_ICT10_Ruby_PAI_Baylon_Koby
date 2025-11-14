from pyscript import display

Cocc = {'Koby', 'Tarcisius', 'Enzo', 'David', 'jamal'}
dance = {'Enzo', 'David', 'Gab', 'Seth', 'Vito'}


display(Cocc | dance, target='output') #Union
display(Cocc & dance, target='output') #Intersection
display(Cocc - dance, target='output') #difference
display(Cocc ^ dance, target='output') #Symmetric Difference/Exclusive OR

