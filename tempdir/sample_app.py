from flask import Flask
from flask import request
from flask import render_template
sample = Flask(__name__)
@sample.route("/")
def main():
    return  render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)


echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile