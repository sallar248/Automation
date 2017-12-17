# script that shows how to parse json

require 'net/http'
require 'json'

url = 'https://ap;i.spotify.com/v1/search?type=artist&q=tycho'
uri = URI(url)
response = Net::HTTP.get(uri)
JSON.parse(response)
