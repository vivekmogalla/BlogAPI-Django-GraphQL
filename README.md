## BlogAPI
simple blog application built with Django and GraphQL

This is a simple blog application built with Django and GraphQL. This application allows users to create, edit, and delete blog posts, as well as add comments to posts.

## Installation
1. Clone the repository to your local machine

2. Install the required dependencies 
   pip install -r requirements.txt

3. Run the migrations:
   python manage.py migrate

4. Start the development server:
   python manage.py runserver
    
## Usage
Once the development server is running, user can access the application by visiting http://localhost:8000 in web browser. From there, User can create new posts, edit existing posts, and add comments to posts.

## API
The application also provides a GraphQL API that can be used to retrieve and manipulate data. The API can be accessed by visiting http://localhost:8000/graphql in your web browser.

Example Queries

```JSON
## Get All Posts
query {
  allPosts {
    id
    title
    description
    publishDate
    author
  }
}
'''

## Get Post by ID
'''
query {
  postById(id: 1) {
    id
    title
    description
    publishDate
    author
  }
}
'''

## CreatePost
'''
mutation {
  createPost(
    title: "My First Post",
    description: "This is my first blog post.",
    author: "John Doe"
  ) {
    post {
      id
      title
      description
      publishDate
      author
    }
  }
}
'''

## UpdatePost
'''
mutation {
  updatePost(
    id: 1,
    title: "My Updated Post",
    description: "This is my updated blog post."
  ) {
    post {
      id
      title
      description
      publishDate
      author
    }
  }
}
'''

## DeletePost
'''
mutation {
  deletePost(id: 1) {
    success
  }
}
'''
