from pathlib import Path

from joblib import dump, load


def save_model(model, filename="iris.joblib"):
    p = Path("model_tabular/")
    p.mkdir(parents=True, exist_ok=True)
    dump(model, Path(f"model_tabular/{filename}"))


def load_model(filename="iris.joblib"):
    return load(Path(f"model_tabular/{filename}"))
