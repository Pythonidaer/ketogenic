print "How old are you?",
age = raw_input()
print "What sex are you?",
sex = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print """
What is your activity level,
ranging from 1 to 5?
Let 1 be highly inactive
and 5 be highly active.
""",
activity = raw_input()
print """
So, you're a %r old %r, 
who is %r tall, weighs %r pounds,
and has an activity level of %r.
""" % (age, sex, height, weight, activity)

# This is my script for python.