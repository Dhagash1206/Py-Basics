import requests

query_text = "{ books { title author } }"  # ask only for the fields needed
response = requests.post("http://localhost:8002/graphql", json={"query": query_text})
print(response.json()["data"])
