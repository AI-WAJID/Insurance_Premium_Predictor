# Insurance Premium Predictor

A Django web application that uses a trained machine learning model to estimate annual health insurance premiums based on user inputs such as age, gender, BMI, number of children, smoker status, and region.

## Features

- Predicts health insurance premium using a Random Forest regression model saved with `joblib`.
- Clean Tailwind CSS–based UI with pages for home, prediction, about, contact, login, and registration.
- Modular Django app structure (`home` app) that is easy to extend with more features.
- Template-driven forms for entering model features (age, sex, BMI, children, smoker, region).

## Tech Stack

- **Backend:** Django
- **Machine Learning:** Scikit-Learn (RandomForestRegressor), joblib
- **Data Handling / Experimentation:** Pandas, Matplotlib (used during model training)
- **Frontend:** Django templates, Tailwind CSS
- **Database:** SQLite (default Django development database)

## Project Structure

```text
Insurance_Premium_Prediction/
├── db.sqlite3                 # Local dev database (can be excluded from Git in production)
├── manage.py
├── home/                      # Django app with views, URLs, etc.
│   ├── views.py               # Includes prediction view that loads and uses the model
│   ├── urls.py
│   └── ...
├── insurance/                 # Project settings & URL routing
│   ├── settings.py
│   └── urls.py
├── model/
│   ├── insurance.csv          # Training dataset
│   ├── Insurance_Premium_Prediction.ipynb  # Notebook used for EDA/model training
│   └── random_forest_regressor            # Trained RandomForestRegressor saved with joblib
├── static/
│   └── home.svg               # Example static asset
└── templates/
    ├── base.html
    ├── index.html
    ├── prediction.html
    ├── about.html
    ├── contact.html
    ├── login.html
    └── registration.html
```

> Note: In a real deployment, you generally should **not** commit `db.sqlite3` or compiled `__pycache__` files. Use a `.gitignore` to exclude them and configure a proper database for production.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AI-WAJID/Insurance_Premium_Predictor.git
cd Insurance_Premium_Predictor
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux / macOS
# source venv/bin/activate
```

### 3. Install dependencies

If a `requirements.txt` file is present:

```bash
pip install -r requirements.txt
```

Otherwise, install the core packages manually, for example:

```bash
pip install django scikit-learn pandas matplotlib joblib
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000/` to access the app.

- Home page: overview of the project.
- `/prediction/`: form for entering user details and viewing the predicted premium.
- `/about/`, `/contact/`: informational pages.
- `/login/`, `/registration/`: auth-related pages (can be wired to Django's auth system for real login/signup).

## Machine Learning Model

The trained model is stored in `model/random_forest_regressor` and loaded in `home/views.py` using `joblib.load(...)`.

**Inputs used by the model:**

- `age`: integer, age of the primary policy holder.
- `sex`: integer (e.g., 1 = male, 0 = female) as encoded during training.
- `bmi`: float, Body Mass Index.
- `children`: integer, number of dependents.
- `smoker`: integer (e.g., 1 = smoker, 0 = non-smoker).
- `region`: integer code representing region (matching the encoding used during training).

The view builds a feature vector from the form data and calls `model.predict([[age, sex, bmi, children, smoker, region]])`, then displays the rounded prediction on the `prediction.html` template.

## Development Notes / Next Steps

- Add a `requirements.txt` file to make environment setup reproducible.
- Exclude development-only files (`db.sqlite3`, `__pycache__`, etc.) via `.gitignore`.
- Wire the `login` and `registration` pages to Django's authentication system for real user accounts.
- Improve validation and UX on the prediction form (e.g., client-side validation, better error messages).
- Deploy the app using a production-ready stack (e.g., Gunicorn + Nginx, or a PaaS like Render/Heroku) with an external database.

## License

Add your preferred license here (for example, MIT) to clarify how others may use or contribute to this project.
