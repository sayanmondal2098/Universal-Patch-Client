# 1. Import the requests library
import requests

URL = "https://gist.githubusercontent.com/sayanmondal2098/99746fb339e5d46d5fffe8356f523ebf/raw/aae6f7a10882cae8b736c0179d3d592aa252c351/ThePatchConfig.config"

# 2. download the data behind the URL
response = requests.get(URL)

# 3. Open the response into a new file called instagram.ico
open("Source.config", "wb").write(response.content)