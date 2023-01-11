import requests


class MySession:

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def get_something(self):
        try:
            response = requests.get(self.url)
            # Check for successful GET request
            if response.status_code == 200:
                website_text = response.text
                return website_text
        except Exception:
            return "Invalid URL"


obj1 = MySession("https://traveltriangle.com/blog/texas-restaurants/")
call_number = 4
while call_number > 1:
    if obj1.get_something() != "Invalid URL":
        print(obj1.get_something())
        print("API call successful in 1st attempt")
        break
    else:
        obj1.get_something()
        call_number -= 1
        print(f"API call successful in 1st attempt {call_number}")
