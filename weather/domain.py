from urlparse import urlparse
parsed_uri = urlparse( 'http://www.cwb.gov.tw/V7/forecast/index.htm' )
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
print domain
