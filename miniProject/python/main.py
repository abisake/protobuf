import sys

import proto.account_pb2 as acc
import proto.user_pb2 as user
import proto.product_pb2 as product
import proto.phone_book_pb2 as phone_book

def account():
    return acc.Account(
        id=99,
        name="Abi",
        is_verified=True,
        follow_ids = [100, 101]
    )

def user1():
    return user.User(
        id=33,
        name="Luffy",
        follows=[
            user.User(id=34, name="Roronoa Zoro"),
            user.User(id=35, name="Vinsmoke Sanji"),
        ]
    )

def user2():
    usr = user.User()
    usr.id=66
    usr.name="Germa Judge"
    usr.follows.add(id=67, name="Reiju")
    usr.follows.add(id=68, name="Sanji")
    return usr
    
def product1():
    return product.Product(
        id=11,
        product_type=product.Product.ProductType.SHIRTS
    )

def product2():
    return product.Product(
        id=12,
        product_type=3
    )

def phone_book1():
    return phone_book.PhoneBook(
        contact_info={
            'Uchicha Itachi'    :   '1234567890',
            'Hatake Kakashi'    :   '3242543632',
        }
    )

def phone_book2():
    ph_book = phone_book.PhoneBook()
    ph_book.contact_info['Zolydck Killua'] ='8923659243'
    ph_book.contact_info['Ging Freeces'] = '3829572034'
    
    return ph_book

if __name__ == "__main__":
    # A map where key=arguments, value=function needs to be called
    functionMap = {
        'account'   :   account,
        'user'      :   user1,
        'user2'     :   user2,
        'product1'  :   product1,
        'product2'  :   product2,
        'phone1'    :   phone_book1,
        'phone2'    :   phone_book2
    }
    
    # on calling this program, more than 2 flags should throw error
    # and print the usable / allowed flags
    if(len(sys.argv) != 2):
        print(f"[main.py] Usable flags [{"|".join(functionMap)}]")
        sys.exit()
        
    # .get() returns if key is present
    # else returns default, which is None, or it can be provided
    # sys.argv[0] is file name
    func = functionMap.get(sys.argv[1], None)
    
    # if no matching func, print the flag as error
    if not func:
        print(f'Unknown flag: \"{sys.argv[1]}\"')
        sys.exit()
        
    print(func())
        
    