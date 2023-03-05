FROM python3.9-nodejs18-alpine

# Install dependencies

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy source code

COPY . .

RUN python3 setup.py

# Run the app

CMD [ "uvicorn", "main:app","--port 8000","--host 0.0.0.0" ]