def warn_the_sheep(queue):
    qu=reversed((queue))
    dt=[]
    for item in qu:
        dt.append(item)
    i=dt.index("wolf")
    if i==0:
        return 'Pls go away and stop eating my sheep'
    else:
        return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(i)
		
#--------------------------
#test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
#test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
#test.assert_equals(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
#test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
#test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')		