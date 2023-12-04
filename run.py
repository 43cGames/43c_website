from app import create_app

"""
pipenv run flask --debug run -h 0.0.0.0
"""

if __name__ == "__main__":
    create_app().run(debug=True)