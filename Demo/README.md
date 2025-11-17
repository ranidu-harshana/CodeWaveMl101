// ...existing code...
# Demo — Sales Prediction App

This demo trains a simple regression model to predict sales from advertising budgets and provides:
- a notebook: [Demo_notebook.ipynb](Demo/Demo_notebook.ipynb)
- a Streamlit UI: [main.py](Demo/main.py)
- dataset: [Advertising Budget and Sales.csv](Demo/dataset/Advertising Budget and Sales.csv)
- trained model: [model.pkl](Demo/model.pkl)
- project settings: [.python-version](Demo/.python-version) and [pyproject.toml](Demo/pyproject.toml)

Important referenced symbols:
- data loader / splitter: [`get_train_test_data`](Demo/Demo_notebook.ipynb)
- runtime model variable: [`model`](Demo/main.py)

Prerequisites
- Python 3.13 (see [.python-version](Demo/.python-version))
- Git (optional, to clone the repo)
- pip or pipx
- Node not required

Quick overview (what you will do)
1. Install `uv` (optional tool) and standard tooling.
2. Create and activate a virtual environment.
3. Install Python dependencies.
4. Run the notebook to inspect / retrain the model.
5. Run the Streamlit UI to interact with the saved model.

1) Install "uv" (optional)
- Option A — install via pipx (recommended for CLI tools):
  - pipx install uv
- Option B — install via pip:
  - python -m pip install uv

(If you don't want `uv`, skip to step 2 and use the standard python venv workflow below.)

2) Create and activate a virtual environment (cross-platform)
- macOS / Linux:
  - python3 -m venv .venv
  - source .venv/bin/activate
- Windows (PowerShell):
  - python -m venv .venv
  - .\.venv\Scripts\Activate.ps1
- Windows (cmd.exe):
  - .\.venv\Scripts\activate.bat

3) Install dependencies
From inside the activated environment, install the packages used in the demo:

- Install directly with pip:
  - python -m pip install --upgrade pip
  - python -m pip install ipykernel joblib kagglehub matplotlib numpy pandas scikit-learn seaborn streamlit jupyterlab

Notes:
- Versions are defined in [pyproject.toml](Demo/pyproject.toml). If you prefer pinned installs, add explicit versions when running pip.

4) Run the notebook (inspect / train / save)
- Start Jupyter Lab:
  - jupyter lab
- Open the notebook file:
  - [Demo_notebook.ipynb](Demo/Demo_notebook.ipynb)
- The notebook contains a helper function [`get_train_test_data`](Demo/Demo_notebook.ipynb) and cells that train and save a LinearRegression model to `model.pkl`.
- To retrain and overwrite the model:
  - run the training cell(s) that contain:
    - model = LinearRegression()
    - model.fit(X_train, y_train)
    - joblib.dump(model, "model.pkl")

5) Run the Streamlit UI
- Ensure `model.pkl` is in the same folder as [main.py](Demo/main.py).
- From the Demo directory and with virtualenv activated:
  - streamlit run main.py
- Open a browser to the address shown (default http://localhost:8501).
- The app uses the runtime variable [`model`](Demo/main.py) loaded with joblib and takes three numeric inputs (TV, Radio, Newspaper budgets) to predict sales.

Example commands (full flow on macOS / Linux)
- git clone <repo>
- cd Demo
- python3 -m venv .venv
- source .venv/bin/activate
- python -m pip install --upgrade pip
- python -m pip install ipykernel joblib kagglehub matplotlib numpy pandas scikit-learn seaborn streamlit jupyterlab
- jupyter lab         # open and run Demo_notebook.ipynb
- streamlit run main.py

Windows PowerShell (example)
- git clone <repo>
- cd Demo
- python -m venv .venv
- .\.venv\Scripts\Activate.ps1
- python -m pip install --upgrade pip
- python -m pip install ipykernel joblib kagglehub matplotlib numpy pandas scikit-learn seaborn streamlit jupyterlab
- jupyter lab
- streamlit run main.py

Troubleshooting
- Model not found: confirm [model.pkl](Demo/model.pkl) is in the Demo folder or re-run training in the notebook to produce it.
- Port in use: streamlit will mention a new port (e.g. 8502); open the indicated address.
- Permission / antivirus issues on Windows: run PowerShell as Administrator if venv activation is blocked (set-executionpolicy may be required).
- Missing packages: install them inside the active venv with pip install <package>.

Tips
- To reproduce exact dependency versions, capture installed versions after setup:
  - python -m pip freeze > requirements.txt
- Use the notebook to explore the dataset: [Advertising Budget and Sales.csv](Demo/dataset/Advertising Budget and Sales.csv)

License
See project LICENSE.

Contact
See repository root for author information.
