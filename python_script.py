import requests

# print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/3662/cmput_404_lab_1/master/python_script.py")

print(r.text)