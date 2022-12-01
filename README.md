# Practicing packaging, containerization and monitoring

This file is a working example of basics of app packaging and containerization. The monitoring part is left as an exercise!

Prepare environment:
```
conda create --name 221203_enseirb --clone base
conda activate 221203_enseirb
pip install -r requirements.txt
```

Run FastAPI app:
```
python app/main.py
```

Build and run Docker app:
```
docker build -t fastapiml .
docker run -d --name fastapiml-app -p 5000:5000 fastapiml
```