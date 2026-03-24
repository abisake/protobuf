import sys

import proto.account_pb2 as acc

def account():
    return acc.Account(
        id=99,
        name="Abi",
        is_verified=True,
        follow_ids = [100, 101]
    )

if __name__ == "__main__":
    # A map where key=arguments, value=function needs to be called
    functionMap = {
        'account' : account
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
        
    