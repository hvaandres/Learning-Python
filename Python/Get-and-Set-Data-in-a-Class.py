class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


uvu = Invoice('UVU', 100)

print(uvu.client)


#Setter Function
uvu.client = 'BYU'

print(uvu.client)