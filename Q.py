print('*'*50)
print(' '*13,end=' ')
print("Project:RETAURANT MANAGEMENT")
print(' '*15,end=' ')
print("WELCOME TO OUR RESTAURANT")
print('*'*50)
print("""            1.          DISHES
                          2.          COOKS
                          3.          ORDER
                          4.          BILL             """)
choice=int(input("What Do You Want To Do?(1/2/3/4)"))
if choice==1:
    DISHES()
elif choice==2:
    COOKS()
elif choice==3:
    ORDER()
elif choice==4:
    BILL()




def DISHES():
    print("lmao")
    insert()
def COOKS():
    print("1.SANJEEV KAPOOR\n 2.VIKAS KHANNA\n 3.RANVEER BRAR\n 4.MOTHER'S SPECIAL\n 5.GORDON RAMSAY")

def ORDER():
    print("nothing")

def BILL():
    print("undefined")
