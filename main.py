from website import create_app

# This is the main file for the website. It is responsible
# for running the website and creating the database if it does not exist.
app = create_app()

# This function is responsible for creating the database if it does not exist.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
