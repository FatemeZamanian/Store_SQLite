from sqlite3 import connect
con=connect("store.db")
cr=con.cursor()

def show_menu():
    print('1-Add new product ')
    print('2-Search ')
    print('3-Edit ')
    print('4-Buy ')
    print('5-Remove ')
    print('6-Show all')
    print('7-Exit ')

def add():
    name=input('enter product name: ')
    price=input('enter product price: ')
    count=input('enter count of this product: ')
    cr.execute(f"INSERT INTO product(name,price,count) VALUES('{name}','{price}','{count}')")

def search():
    id=int(input('enter valid id: '))
    cr.execute(f'SELECT * FROM product WHERE product.id={id}')
    res = cr.fetchone()
    if res == None:
        return None
        print('not found..!')
    else:
        return id
        print(res)

def edit():
    id=search()
    if id != None:
        name = input('enter product name: ')
        price = input('enter product price: ')
        count = input('enter count of this product: ')
        cr.execute(f"UPDATE product SET name='{name}',price='{price}',count='{count}' WHERE product.id='{id}'")
    else:
        print('not found record...')


def buy():
    id = search()
    if id != None:
        count = int(input('enter count of this product: '))
        cr.execute(f"SELECT * FROM product WHERE id={id}")
        c=cr.fetchone()
        if int(c[3])>=count:
            c_new=int(c[3])-count
            cr.execute(f"UPDATE product SET count='{c_new}' WHERE product.id='{id}'")
        else:
            print('this product is not enough....')
    else:
        print('not found record...')

def remove():
    id = search()
    if id != None:
        cr.execute(f'DELETE FROM product WHERE product.id={id}')
    else:
        print('not found record...')

def show():
    cr.execute("SELECT * FROM product")
    res=cr.fetchall()
    for i in res:
        print(i)

while True:
    show_menu()
    user=int(input())

    if user==1:
        add()

    elif user==2:
        search()
    elif user==3:
        edit()
    elif user==4:
        buy()
    elif user==5:
        remove()
    elif user==6:
        show()
    elif user==7:
        a=input('save changes ? (y/n)')
        if a=='n':
            con.close()
            exit()
        elif a=='y':
            con.commit()
            con.close()
            exit()