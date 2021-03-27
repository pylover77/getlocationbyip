import pygeoip
## getting location by ip using pygeoip lib 
## pip install pygeoip

class getlocation:
    def search(self):
        self.geofile = pygeoip.GeoIP("GeoLiteCity.dat")
        self.ip = input("IP Address:")
        self.response = self.geofile.record_by_addr(self.ip)
        for a, b in self.response.items():
            print(f'{a} : {b}') 

if __name__ == '__main__':
    local = getlocation()
    local.search()

