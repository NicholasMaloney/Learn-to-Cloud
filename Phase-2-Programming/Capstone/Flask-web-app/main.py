from website import create_app

app = create_app()

if __name__ == '__main__': #Only start the web app if we run the file directly.
    app.run(debug=True) # Starts the web app 
