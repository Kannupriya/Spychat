print "Let\'s get started"
spy_name = input("What is your name?")
spy_age = 0
spy_rating = 0.0
spy_is_online = False

if len(spy_name) > 0:
    print "Welcome"+" "+spy_name+"!"
    spy_salutation = input("What do you prefer to write(Mr. or Ms.)?")
    spy_name = spy_salutation + spy_name
    print "Alright " + spy_name + ".Let me know more about you"
    spy_age = input("What is your age?")
    if spy_age > 18 and spy_age < 50:
        print "Congracts ! Yor are eligible and you can move ahead"
        spy_rating = input("What is your spy rating ? ")
        if spy_rating > 4.5:
            print "Great Job !"
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
            spy_is_online = True
            print "Authentication now completes. Welcome " + spy_name + " age: " + spy_age + " and rating of: " + spy_rating + " Proud to have you onboard"
        else:
            print 'We can always use somebody to help in the office.'

    else:
        print "Sorry ! You are not eligible !"
else:
    print "Please enter the name"