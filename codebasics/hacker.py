import os

email = os.getenv("DJANGO_EMAIL")
password = os.environ.get("DJANGO_PASSWORD")

print(email)
print(password)


import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

print('env email and password')
print(env("DJANGO_EMAIL"))
print(env("DJANGO_PASSWORD"))