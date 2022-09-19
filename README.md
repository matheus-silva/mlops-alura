mlops-alura-deploy
==============================

Project created during Alura's MLOps course, which covered the following subjects: 

* Serve Machine Learning models through APIs using _flask_
* Use _cookiecutter_ to organize this repository
* Use three different strategies to deploy this application:
   1. Deploy using GCP Compute Engine (Virtual Machines)
   2. Deploy using GCP App Engine (Serverless)
   3. Deploy using Docker (Container)
* Apply _continuous delivery_ (CD) using GitHub Actions

How to run this project in development
------------

Use the following steps to run this project in a development environment:

1. Activate the virtual environment:
    
    ```sh
    source ./venv/bin/activate
    ```

2. Export the following environment variables:

    ```sh
    export PORT=5000
    export BASIC_AUTH_USERNAME=your_username
    export BASIC_AUTH_PASSWORD=your_password
    ```

3. Run API:

    ```sh
    gunicorn -b :$PORT src.app.main:app
    ```

How to run this project in APP Engine 
------------

Use the followings steps to run this project in APP Engine:

1. Create a new environment variable file from `app_env_vars.yaml.example`:
    ```sh
    cp app_env_vars.yaml.example app_env_vars.yaml
    ```

2. Edit the variables defined in `app_env_vars.yaml`:

3. Deploy your application to APP Engine using [gcloud](https://cloud.google.com/sdk/docs/install?hl=pt-br#windows):

    ```sh
    gcloud app deploy
    ```

How to run this project in Docker
------------

Use the followings steps to run this project in Docker:

1. Build Docker image:

    ```sh
    docker build -t mlops-alura --build-arg BASIC_AUTH_USERNAME_ARG=your_username --build-arg BASIC_AUTH_PASSWORD_ARG=your_password .
    ```

2. Run Docker container:

    ```sh
    docker run -p 5000:5000 mlops-alura
    ```

How to run this project in Docker + Cloud Run through GitHub Actions
------------

1. Add the following secrets in the GitHub Repository: 

   | Secret              | Description                        |
   |---------------------|------------------------------------|
   | BASIC_AUTH_USERNAME | Username used in the API           |
   | BASIC_AUTH_PASSWORD | Password used in the API           |
   | RUN_PROJECT         | GCP Project ID                     |
   | RUN_SA_KEY          | GCP Service Account key            |

2. Manually trigger this pipeline or push a new commit in the expected branch.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
