# Properties and Decorators

# Decorators: Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

# Properties: In Python, the main purpose of Property() function is to create property of a class. Return: Returns a property attribute from the given getter, setter and deleter. Note: If no arguments are given, property() method returns a base property attribute that doesn't contain any getter, setter or deleter.


class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'
    # This is called decorator and it means that I will have access to the name of the client. If I don't have a decorator information it's because this data is only for internal purpose. 
    @property
    def client(self):
        return self._client
    
    # This property "setter" will allow us to override the name of our client.
    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total

uvu = Invoice('UVU', 100)

print(uvu.client)

uvu.client = 'BYU'

print(uvu.client)

