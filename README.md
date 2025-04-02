# test_back_5D

## FastAPI+SQLModel test issue

### Description

The API provides functionality for working with shortened URLs:

1. Creating a new shortened URL

2. Viewing the list of all saved URLs

3. Redirecting from the shortened URL to the original one

### Usage Example 

Creating a shortened URL:

POST http://127.0.0.1:8080?str_url=https://example.com

Getting the list of URLs:

GET http://127.0.0.1:8080/urls_list

Redirecting:

GET http://127.0.0.1:8080/?short_id=abcde

## Install and run:

### To access via port 8080, open it in the firewall:

sudo ufw allow 8080

### Build and run the container:

docker-compose up --build

## The server is running at:: http://127.0.0.1:8080/
## Interactive mode: http://127.0.0.1:8080/docs#
