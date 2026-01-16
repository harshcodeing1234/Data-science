# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

class demo:
    def __init__(harsh,name):
        harsh.name = name
    def greet(harsh):
        print(f"Hello, {harsh.name}!")
    
d1 = demo("Harsh")
d1.greet()