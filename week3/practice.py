""""print("Zain Durrani")
def name_write():
    print("zaindurrANI IS ZAINDURRANI")
name_write()"""
my_global = 10
def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print("Access to Global",my_global)
        print("Access to enclosed", enclosed_v)
    fn2()    
fn1()

