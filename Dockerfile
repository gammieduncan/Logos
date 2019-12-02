FROM python:3.7

WORKDIR /usr/src/app

# Copy all files into /usr/src/app
COPY . .

# Replace URL in config.py with "URL = ${URL}" at line 25
RUN sed -i "25s/.*/URL = 'http:\/\/localhost:3000'/" app/config.py

# Replace DB_TYPE in config.py with "DB_TYPE = 'sqlite'" at line 9
RUN sed -i "9s/.*/DB_TYPE = 'sqlite'/" app/config.py

RUN chmod +x ./install.sh

# Run install script
RUN ./install.sh -y

RUN python3 "$(pwd)"/app/utilities/create_db.py

CMD python3 app/run.py
