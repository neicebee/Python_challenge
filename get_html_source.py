import requests

class get_html:
    def __init__(self, url: str) -> None:
        if not url:
            self.url = None
            return
        self.url = url
        self.hdr = {'Accept-Language': 'ko_KR,en;q=0.8', \
            'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; \
                Nexus 5 Build/MRA58N) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile \
                        Safari/537.36')}
    
    def get_req(self) -> str or int:
        if not self.url:
            return None

        with requests.Session() as s:
            req = s.get(self.url, headers=self.hdr)

            if not req.status_code == 200:
                return req.status_code

            return req.text
    
    def get_content(self) -> bytes or int:
        if not self.url:
            return None
        
        with requests.Session() as s:
            req = s.get(self.url, headers=self.hdr)

            if not req.status_code == 200:
                return req.status_code
    
            return req.content
        
    def check_url(self) -> str:
        return self.url
    
    def change_url(self, url: str) -> None:
        if not url:
            return
        self.url = url