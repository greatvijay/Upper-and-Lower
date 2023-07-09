def string_test(s):
    upper_case=0
    lower_case=0
    for c in s:
        if c.isupper():
           upper_case+=1 #counting upper case
        elif c.islower():
           lower_case+=1  #counting lower case
        else:
           pass
    print ("Entered String : ", s)
    print ("No. of Upper case characters : ", upper_case)
    print ("No. of Lower case Characters : ", lower_case)

string_test('The quick Brown Fox')