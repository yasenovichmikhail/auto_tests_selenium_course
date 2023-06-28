def chunked(st, n):
    st = st.split()
    a = [[] for _ in range(0, len(st), n)]
    for i in range(len(a)):
        a[i].extend(st[:n])
        st = st[n:]
    return a

string = 'a b c d e f'
num = 2

chunked(string, num)