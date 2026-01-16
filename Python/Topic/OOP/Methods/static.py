# static methods : Sometimes we need a function that does not use the self-parameter.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3


