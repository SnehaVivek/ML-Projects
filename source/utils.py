import os
import pickle

try:
    import dill as serialization_lib
except Exception:
    serialization_lib = pickle


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            serialization_lib.dump(obj, file_obj)

    except Exception as e:
        raise RuntimeError(f"Failed to save object to {file_path}: {e}") from e