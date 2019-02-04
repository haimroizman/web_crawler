# Onion Web Crawler

The crawler crawls the site : http://nzxj65x32vh2fkhk.onion/all and stores the most recent 'pastes'

## Getting Started

Start typing the following commands from the terminal:
```

# loads the image to the docker image repository
sudo docker load -i ./web-crawler-image.tar

# get the image ID from the image list
sudo docker images

# run the web-crawler image using its ID
docker run -d -p 8118:8118 -p 9050:9050 [image ID of haim/web-crawler repository]

# get the container ID from the container list
sudo docker ps

# login into the container
sudo docker exec -it [container ID] /bin/bash

# run the web crawler
cd ~/web_crawler
python3 main.py

# you will see some prints of the "pastes" objects, those that are being saved to the database.
```