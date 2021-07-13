'''
This is a python class in one line using type meta class.
Example usage:

robo = Robot()
robo.say_hello("Anyesh")

Output: Hi, I am Anyesh
'''

Robot = type("Robot", (), { "say_hello": lambda self, name: "Hi, I am " + name, },)