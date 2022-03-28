from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    #name = "tim"
    
   #return '''
   # <html>
    
       # <h1>Hello, '''  + name + '''!</h1>
    
    #</html>'''
    user = "Jaskaran"
    return '''
    <html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
        <h1>Hello, '''  + user +'''!</h1>
        <p> <a href = "https://www.google.com" >not google</a> </p>
        <p> <ul>  <li> Paris </li> <li> London </li> <li> Rome </li> <li> Tahiti </li> </ul> </p>
                
    </body>
    </html>'''
    
    
   
if __name__ == '__main__':
    app.run()
