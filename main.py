from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # Everyy time there is a change in the code, the file will be rerun automatically.

