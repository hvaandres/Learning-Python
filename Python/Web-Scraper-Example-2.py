from bs4 import BeautifulSoup
html_doc = """<!DOCTYPE html>
<html>

<head>
    <title>I love this example </title>
</head>

<body>
    <p id="elegant"> I am Andres Haro </p>
    <p id="super"> I love coding</p>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

for paragraph in soup.find_all('p'):
    print(paragraph.get_text())
