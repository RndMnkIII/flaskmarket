from market import app

#Checks if the run.py file has executed directly and not imported
if __name__ == "__main__":
    app.run(host='rndmnkiii.com', port='4000', debug=True)