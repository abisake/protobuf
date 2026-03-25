import sys

import proto.account_pb2 as acc
import proto.user_pb2 as user
import proto.product_pb2 as product
import proto.phone_book_pb2 as phone_book
import google.protobuf.field_mask_pb2 as field_mask
import google.protobuf.wrappers_pb2 as wrappers


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

def field_mask1():
    # field mask is way to hide or remove some fields from a message
    # ideal when you multiple clients, not everyone needs all the data
    account1 = account()
    print(account1)  # for dedbugging
    # mention the field name that needs to visible
    mask = field_mask.FieldMask(paths=
        ['id', 'name']
    )
    
    # create an another message, where the masked structure will be stored
    account1Result = acc.Account()
    
    mask.MergeMessage(account1, account1Result)
    
    return account1Result

def field_mask2():
    # we can merge two field mask into a mask, by doing union of the two masks
    acc1 = account()
    print(acc1)
    
    mask1 = field_mask.FieldMask()
    mask1.FromJsonString('id,name')
    mask2 = field_mask.FieldMask()
    mask2.FromJsonString('id,followIds') # in proto it was follow_ids, 
    # but in json field name will be in camelCase
    
    mask3 = field_mask.FieldMask()
    mask3.Union(mask1, mask2)
    
    accResult1 = acc.Account()
    mask3.MergeMessage(acc1, accResult1)
    return accResult1
    
def wrapper():
    return [
        wrappers.BoolValue(value=True),
        wrappers.BytesValue(value=b'This a byte string'),
        wrappers.DoubleValue(value=31240421),
        wrappers.FloatValue(value=3.14),
        # many more wrappers
    ]

def file():
    # we serialize a proto message into a .bin file and 
    # deserialize it, the content should match
    acc1 = account()
    # output file
    path = 'account.bin'
    
    print(f"Converting and writing into bin ------\n{acc1}")
    with open(path, 'wb') as bin:
        # output will be bytes string
        bytes_str = acc1.SerializeToString()
        bin.write(bytes_str)
    
    print("Data is successfully converted and stored-------")
    
    print("Reading from file------")
    with open(path, 'rb') as bin:
        acc1 = acc.Account().FromString(bin.read())
        
    print(f"Data is {acc1}")
    print("Done")
            

if __name__ == "__main__":
    # A map where key=arguments, value=function needs to be called
    functionMap = {
        'account'   :   account,
        'user'      :   user1,
        'user2'     :   user2,
        'product1'  :   product1,
        'product2'  :   product2,
        'phone1'    :   phone_book1,
        'phone2'    :   phone_book2,
        'field1'    :   field_mask1,
        'field2'    :   field_mask2,
        'wrappers'  :   wrapper,
        'file'      :   file,
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
        
    