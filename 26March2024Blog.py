from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now()
        
    def __str__(self):   
        return  f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.date}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []
        
    def add_post(self,post):
        if (post.title in [post.title for post in self.posts]):
            raise ValueError("A post with the same title already exists.")
        else:
            self.posts.append(post)
            return True
            
    
    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                return True, post
        raise ValueError("No post with the given title found to delete.")
            
                      
    def list_post(self):
        if not self.posts:
            raise ValueError("Nothing to display")
        else:
            for post in self.posts:
                yield post

blog = Blog()  # Create the Blog object outside the while loop

flag = True
while flag:
    choice = input("\nChoices:\nPress (a) to add post\nPress (d) to delete post\nPress (l) to display posts\nPress (q) to exit\n\nEnter the choice: ").lower()
    
    if choice == 'a':
        title = input("Enter the title: ")
        content = input("Enter the content: ")
        author = input("Enter the name of author: ")
        
        try:
            if blog.add_post(Post(title, content, author)):
                print(f'Successfully added post {title}')
        except ValueError as e:
            print(e)
            
    elif choice == 'd':
        delete_title = input("Enter the title of the post you want to delete: ")
        
        try:
            d, s = blog.delete_post(delete_title)
            if d:
                print(f"Successfully deleted the post '{s.title}'")
        except ValueError as e:
            print(e)
            
    elif choice == 'l':
        try:
            for post in blog.list_post():
                print(post)
        except ValueError as e:
            print(e)
            
    elif choice == 'q':
        flag = False
    else:
        print("Unknown choice")

		
 

        
	
    
	    
             
	    
	        