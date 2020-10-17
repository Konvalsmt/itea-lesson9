def ch(two):
    z=0
    for i in two:
        z+=int(i)
    print(z)    
    if len(str(z))>1:
        r=ch(str(z))
    else:
        r=z
    return r   

def life_path_number(birthdate="1879-03-14"):
    yy=birthdate[0:4]
    mm=birthdate[5:7]
    dd=birthdate[8:10]
    z=0
    for i in yy:
        z+=int(i)
    if len(str(ch(str(z))+ch(str(mm))+ch(str(dd))))>1:
        res=ch(str(ch(str(z))+ch(str(mm))+ch(str(dd))))
    else:
        res=ch(str(z))+ch(str(mm))+ch(str(dd))
    return res  
	
	
	
	
#----------------------------------------------
	
#import codewars_test as test

#from solution import life_path_number

#@test.describe("Example")
#def test_group():
#    @test.it("Life Path Number - Bill Gates")
#    def billy():
#        test.assert_equals(life_path_number("1955-10-28"), 4)
#    
#    @test.it("Life Path Number - Elon Musk")
#    def elly():
#        test.assert_equals(life_path_number("1971-06-28"), 7)
	