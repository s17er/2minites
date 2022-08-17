import urllib3

http = urllib3.PoolManager(
    num_pools=4,
    timeout=urllib3.Timeout(connect=10.0, read=30.0)
)

def scrape(url):
    response = http.request('GET', url, retries=2, redirect=True)
    if response.status != 200:
        print('status error. %s' % response.status)
        return
    
    
if __name__ == '__main__':
    scrape('https://kknews.cc/sports/k9mnq.html')