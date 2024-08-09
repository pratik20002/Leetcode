class Codec:
    def __init__(self):
        self.valueDict = {}
        self.url_prefix = "http://tinyurl.com/"
    
    def generate_key(self) -> str:
        """Generate a unique key for the shortened URL."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        key = self.generate_key()
        while key in self.valueDict:
            key = self.generate_key()  # Ensure the key is unique
        
        self.valueDict[key] = longUrl
        return self.url_prefix + key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        key = shortUrl.replace(self.url_prefix, "")
        return self.valueDict.get(key, "")