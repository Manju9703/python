def check():
    a=str(input("Enter the first word:"))
    b=str(input("Enter the second word:"))
    if(sorted(a)==sorted(b)):
        print("Entered text is an anagram")
    else:
        print("Entered text is not an anagram")
check()
