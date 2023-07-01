FROM python:3.8-slim-buster

# establishing the work dir
WORKDIR /app

# upgrading pip
RUN python -m pip install --upgrade pip


# installing the requirements
COPY ./requirements.txt .
RUN pip install -r  requirements.txt

# copy all other files
COPY . .
# exposing the port
EXPOSE 5001

# # Creating an entrypoint
ENTRYPOINT ["python"]

# # running the end command
CMD ["app.py"]
