print "lets get started..."
while True:
    try:
        name = raw_input("what is your name ")
        if len(name)>0:
            print "welcome "+" "+ name+ " "+ "glad to see u back"
            break
    except:
        print "enter a valid username "