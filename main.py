c=0
hi = 'Hello World'
for l in hi:
    print(' '*c+l)
    c+=1
    if l == ' ':
        c=0