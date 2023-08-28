import requests

text = input('ASCII Art Text > ')

r = requests.get('http://artii.herokuapp.com/make?text=Awesomesauce')
print(r.text)