

import re

def dad_filter_regex(st):
    return re.sub(r",+", "!", st)






def dad_filter(st):
    while ",," in st:
        st = st.replace(",,", ",")
    return st
res = dad_filter("asdasd,'sad,asdd,asd,,a,ad,,asdas,,,,, asdd,dasd,,,")
print(res)  