import turtle

def capitalOregon():
    #Quiz
    correct_answer = "salem"
    attempts = 3

    for i in range(attempts):
        user_answer = input("What is the capital of Oregon? ").strip().lower()
        if user_answer == correct_answer:
            print("Correct!")
            break
        else:
            if i < attempts - 1:
                print("Try Again!")
            else:
                print("Out of attempts! The capital is Salem.")
                exit()

    #Turtle Settings
    screen = turtle.Screen()
    screen.title("Oregon Outline")

    t = turtle.Turtle()
    t.speed(3)

    #Turtle Drawing
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(410)
    t.right(90)
    t.goto(-150, 100)

    # Mark Salem (approximate location)
    t.penup()
    t.goto(-110, 0)
    t.dot(12, "red")
    t.write(" Salem", font=("Arial", 12, "bold"))

def capitalFlorida():
    ## Tony Hogston
    ## State of Florida Quiz with Turtle Graphics

    # Clear screen
    turtle.clear()

    # Create screen with Orange background
    screen = turtle.Screen()
    screen.bgcolor("orange")
    turtle.pencolor("green")

    # Quiz popup, two guesses gllowed, multiple mccepted spellings in the event the user doesn't type exactly as listed.
    correct_answers = ["Tallahassee", "TALLAHASSEE", "tallahassee"]
    guesses = 0
    user_correct = False

    while guesses < 2 and not user_correct:
        answer = screen.textinput(
            "The Sunshine State Quiz",
            "What is the capital of Florida?\n\n"
            "Miami\nTallahassee\nOrlando\nFt. Lauderdale\nTampa\n\n"
            f"Guess {guesses+1} of 2 — Type your answer exactly as shown:"
        )

        if answer in correct_answers:
            user_correct = True
        else:
            guesses += 1

    # Correct Answer, Draw the State of Florida
    if user_correct:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pencolor("blue")
        turtle.pensize(3)
        turtle.pendown()

        turtle.shape("turtle")
        turtle.speed(3)

        # Draw the State of Florida
        turtle.forward(95)
        turtle.right(80)
        turtle.forward(5)
        turtle.left(80)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(70)
        turtle.forward(200)
        turtle.right(40)
        turtle.forward(10)
        turtle.right(30)
        turtle.forward(20)
        turtle.right(40)
        turtle.forward(10)
        turtle.right(35)
        turtle.forward(50)
        turtle.right(30)
        turtle.forward(65)
        turtle.right(20)
        turtle.forward(30)
        turtle.left(20)
        turtle.forward(60)
        turtle.left(70)
        turtle.forward(60)
        turtle.left(45)
        turtle.forward(30)
        turtle.right(125)
        turtle.forward(30)
        turtle.left(70)
        turtle.forward(55)
        turtle.right(110)
        turtle.forward(10)
        turtle.goto(0, 0)

        # Circle marking Tallahassee
        turtle.penup()
        turtle.goto(105, -17)
        turtle.pendown()
        turtle.circle(3)

        # Centered correct message
        turtle.penup()
        turtle.goto(0, 200)   # centered horizontally
        turtle.pendown()
        turtle.write("You are correct! The capital of Florida is Tallahassee.", align="center", font=("Arial", 14, "normal"))
        turtle.penup()
        turtle.goto(0,10)

    # Incorrect answer, output and end
    else:
        turtle.penup()
        turtle.pencolor("red")
        turtle.goto(0, 0)     # center of screen
        turtle.pendown()
        turtle.write("Sorry, better luck next time.", align="center", font=("Arial", 12, "normal"))

def capitalTexas():
    correct_answers = ["austin"]
    capital = "AUSTIN"
    attempts_allowed = 3

    t.clear()
    t.penup()
    t.goto(-160, 120)
    t.write("Texas Capital Quiz", font=("Arial", 18, "bold"))

    for attempt in range(1, attempts_allowed + 1):
        answer = input("What is the capital of Texas? ").lower().strip()

        if answer in correct_answers:
            t.clear()
            t.penup()
            t.goto(-180, 130)
            t.write("Correct! Austin is the capital of Texas.", font=("Arial", 14, "bold"))

            # Draw a simple outline of Texas
            texas_outline = [
                (-90, 90),    # top left panhandle
                (20, 90),     # top right panhandle
                (20, 45),     # down panhandle
                (65, 45),     # east edge
                (95, 10),     # northeast curve
                (75, -35),    # east/southeast
                (45, -65),    # Gulf coast
                (25, -105),   # south Texas point
                (-10, -75),   # southwest
                (-45, -95),   # west bend
                (-80, -45),   # west side
                (-120, -20),  # far west point
                (-95, 30),    # northwest edge
                (-90, 90)     # back to start
            ]

            t.goto(texas_outline[0])
            t.pendown()

            for point in texas_outline:
                t.goto(point)

            t.penup()

            # Mark Austin with a small dot
            t.goto(-10, -20)
            t.dot(8)
            t.goto(0, -35)
            t.write("Austin", font=("Arial", 10, "normal"))

            return True

        elif attempt < attempts_allowed:
            print("Incorrect. Try again.")

            # Nested loop reveals a letter-by-letter hint
            hint = ""

            for i in range(attempt):
                for letter in capital[i]:
                    hint += letter

            print("Hint:", hint + "_" * (len(capital) - len(hint)))

        else:
            t.clear()
            t.penup()
            t.goto(-190, 50)
            t.write("Incorrect. The capital of Texas is Austin.", font=("Arial", 14, "bold"))

            return False

def main():
    Correct = bool()

    
