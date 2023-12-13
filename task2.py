x=input("ENTER THE ETHEREUM ADDRESS : ")
if x.startswith("0x") and len(x)==42 and all(c in "0123456789abcdefABCDEF" for c in x[2:]):
    print("ETHEREUM ADDRESS IS VALID")
else:   
    print("ETHEREUM ADDRESS IS NOT VALID")