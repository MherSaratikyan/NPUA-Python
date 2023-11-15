import requests

base_url = "https://jsonplaceholder.typicode.com/"

fetched_posts = requests.get(f"{base_url}/posts")

if fetched_posts.status_code == 200:
    posts = fetched_posts.json()

    #filtering the titles
    filtered_titles = []
    for post in posts:
        if len(post['title'].split()) <= 6:
            filtered_titles.append(post['title'])

    print("Titles with less than or equal to 6 words:")
    
    for title in filtered_titles:
        print(title)

    #filtering the posts
    filtered_posts = []

    for post in posts:
        if len(post['body'].split('\n')) <= 3:
            filtered_posts.append(post)
    
    print("\nPosts with body containing 3 or fewer lines:")
    for post in filtered_posts:
       print(f"\nTitle: {post['title']}")
       print(f"Body:\n{post['body']}")
else:
    print(f"Failed to fetch posts.")

my_post = {"title": "My Title", "body": "Some text"}
response = requests.post(f"{base_url}/posts", json = my_post)

if response.status_code == 201:
    my_post_id = response.json()['id']
    print(f"ID of my_post: {my_post_id}")

my_updated_post = {"title": "Updated title", "body":"Some updated text"}
response = requests.put(f"{base_url}/posts/{my_post_id}", json = my_updated_post)

if response.status_code == 200:
    print("The post my_post updated successfully")

response = requests.delete(f"{base_url}/posts/{my_post_id}")
if response.status_code == 200:
    print("The post my_pots deleted successfully")
