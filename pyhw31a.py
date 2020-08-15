## my game
print(" ")
print(" ")
print("Welcome to Ron's sweet choose your own adventure game.")
print("You have arrived at an abandoned amusement park.")
print("Just like Scooby Doo.  What do you want to do first?")
print("1. Play the arcade games.")
print("2. Ride the rollercoaster.")
print("3. Bump the bumpercars.")

first = input(">>> ")

if first == "1":
    print("'Let us see if I still got it,' you say to no one in particular.")
    print("1. Ring toss.  I can get it with ten tosses, tops.")
    print("2. Knock down the pins.  Yep, I was pretty trusty with a baseball in my day.")

    games = input(">>> ")

    if games == "1":
        print("Tossing the rings, when all of a sudden, a ghost!")
        print("1. Holy mackeral! Run!")
        print("2. Get him!")

        ghost = input(">>> ")

        if ghost == "2":
            print("You chase the ghost Scooby Doo-style, running back and forth across the frame.")
            print("But then the ghost remembers he's there to scare _you_, so he turns all dark and scary.")
            print("1. Stand tall, or 2. Run scooby doo style with him chasing you now.")

            ghost2 = input(">>> ")

            if ghost2 == "1":
                print("The ghost is real mad now.  The figure looms over you, and the sky turns grim.")
                print("He pulls out a knife.  ..wait a minute.  A ghost doesn't need a knife.")
                print("You pull off his mask.  Old Man Danvers! you exclaim.  You win.")
            elif ghost2 == "2":
                print("You run scooby doo style with him chasing you now.")
                print("Then you remember about how you didn't claim your prize at the ring toss.")
                print("You go back and pick out the best prize there, a fill in the blank.  You win.")
            else:
                print("You can't do that!  Boo!  You lose!")
        elif ghost == "1":
            print("You run away, and with some dipping and dodging you get away.")
            print("You make your way to the concession stand.")
            print("1. Get something to eat.  2. Ghost food?  Are you nuts?")

            food = input(">>> ")

            if food == "1":
                print("You get ghost food poisoning and die.  You lose.")
            else:
                print("Second smart thing you did today.  You win.")
        else:
            print("You can't do that!  You lose!")
    elif games == "2":
        print("Let's see how the fastball is today, you say to no one in particular again.")
        print("You approach the booth, and the carnie manning the pins is a ghoul, but he seems friendly enough.")
        print("He says 'Three pitches for a fiver.'")
        print("And you say, five bucks! well I never.")
        print("And he says, well, there's another way.")
        print("Give me your soul and you can have as many pitches as you want.")
        print("1. Pay the five bucks, it's not that unreasonable, considering this amusement park is haunted.")
        print("2. Play for your soul.")

        pitches = input(">>> ")

        if pitches == "1":
            print("You knock down all the pins on your first throw!  You win.")
        elif pitches == "2":
            print("Boo!  You lose.")
        else:
            print("You can't do that!  You lose.")
    else:
        print("You can't do that!  You lose.")

elif first == "2":
    print("Let's ride the rollercoaster!  But which one?")
    print("1. Space Mountain.")
    print("2. The BEast.")

    coaster = input(">>> ")

    if coaster == "1":
        print("Space Mountain over the Beast?  You lose.")
    elif coaster == "2":
        print("Best roller coaster evah!  You win.")
    else:
        print("You can't do that! You lose.")
elif first == "3":
    print("You make your way to the bumpercars, and see that there is a wait in line.")
    print("You get to the end of the line, behind a family of skeleton people.")
    print("Do you: 1. Wait patiently? or")
    print("2. Cut to the front of the line.")

    line = input(">>> ")

    if line == "1":
        print("You wait in line patiently, and it turns out the skeletons are really nice.")
        print("You bump in the bumpercars with an assortment of characters.")
        print("They even let the time go longer, seeing as that you are not undead.  You win.")
    elif line == "2":
        print("You cut ahead.  You get on like one grouping of people faster.")
        print("But you get a busted car, and it won't go straight or fast.  You lose.")
    else:
        print("You can't do that!  You lose.")
else:
    print("You can't do that!  You lose.")
