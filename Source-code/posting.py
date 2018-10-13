class post_(object):
    def __init__(self, title,content,author,blog_id,post_id,date):
        self.title = title              #"This is my first title with mongo"
        self.content = content        # post id for identify the post
        self.author = author         
        self.blog_id = blog_id
        self.post_id = post_id
        self.date = date

def save_to_mongo(self):
    Databse.insert(collection='post',data=self.json)

def json(self):
    return{
        'id':self.post_id,
        'author':self.author,
        'title':self.title,
        'blog_id':self.blog_id,
        'content':self.content,
        "created_date":self.date
    }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts',query={'id':id})
        
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='post',query={'blog_id'})]