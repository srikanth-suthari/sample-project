import urllib.request

class URLHandler:
    def open(self, url):
        try:
            with urllib.request.urlopen(url) as response:
                content = response.read()
                print(content[:100])  # Print the first 100 bytes of the response
        except Exception as e:
            print(f"Error opening URL: {e}")

# Example usage
handler = URLHandler()
handler.open("https://www.google.com")
