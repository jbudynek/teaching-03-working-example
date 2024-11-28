# Practicing packaging, containerization and monitoring

This file is a working example of basics of app packaging and containerization.
The monitoring part is left as an exercise!
See instructions at: <https://github.com/jbudynek/teaching-03-template>

Prepare environment:

```bash
conda create --name YYMMDD_ia_course --clone base
conda activate YYMMDD_ia_course
pip install -r requirements.txt
```

Run FastAPI app:

```bash
python app/main.py
```

Build and run Docker app:

```bash
docker build -t fastapiml .
docker run -d --name fastapiml-app -p 5000:5000 fastapiml
```

## Notes

Used in 2022, 2023 and 2024 with AI engineering students in Bordeaux.
