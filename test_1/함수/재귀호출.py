import string
import time as t

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    t.sleep(1)
    print("in number : num = {}, base = {}".format(num, base))
    q, r = divmod(num, base)
    print("q, r in number : divmod({}, {}) = 몫:{}, 나머지:{}".format(num, base, q,r))
    t.sleep(1)
    if q == 0 :

        return tmp[r]
    else :
        return convert(q, base) + tmp[r]
    
print(convert(10,2))