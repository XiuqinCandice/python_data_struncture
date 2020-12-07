def hash_module(key,size):
    return key % size #the index size will stay between 0 and table_size - 1

def hash_trunc(key):
    return key % 1000 #will give us a key of up to 3 digits

def hash_fold(key, chunk_size):
    str_key = str(key)
    print('Key: ' + str_key)
    hash_val = 0
    print('Chunk:')
    for i in range(0,len(str_key),chunk_size):

        if i+chunk_size < len(str_key):

            print(str_key[i:i+chunk_size])
            hash_val += int(str_key[i:i+chunk_size])
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val

lst = [None]*10
key = 35
index = hash_module(key, len(lst))
key1 = 1234567
index1 = hash_trunc(key1)
key2 = 345678910
chunk_size = 2
print('The index for key ' + str(key) + ' is ' + str(index))
print('The index for key after truncation ' + str(key1) + ' is ' + str(index1))
print('Hash Key:' + str(hash_fold(key2, chunk_size)))