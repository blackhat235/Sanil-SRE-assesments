FROM python

WORKDIR /random-app
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

#this runs when image is built
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

ENTRYPOINT [ "python" ,"app.py" ]
