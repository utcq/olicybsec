data = "it04nd_11ls4_vn_33vd31rs__tthn33_1sl0cl{uCtE1S0AnT!I}" 

secret = ['a']*(len(data)-1)

i=0
j=len(data)-1
k = False
while j - i >= 0:
    if k:
        i += 1
        k = False
    else:
        j -= 1
        k = True
    secret[i if k else j] = data[j-i]
secret[26] = 'i'; secret.append('}')
print(''.join(secret))
