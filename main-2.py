import requests


class MySession:
    def __init__(self, url):
        self.url = url

    def __enter__(self):
        try:
            self.response = requests.get(self.url)
            self.response.raise_for_status()
            return self.response.text
        except Exception:
            return "Invalid URL"

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


call_number = 3
while call_number:
    with MySession("https://www.google.com") as website_text:
        if website_text != "Invalid URL":
            print("API Genarated Sussfully")
            break
        else:
            call_number -= 1
            print(f"API is unsuccesfull in {call_number+1} attempts")
