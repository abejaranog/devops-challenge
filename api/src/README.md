### Run the app

If you want to run the app locally:

```bash
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ export PSQL_URI=postgres://<username>:<password>@<db_host>:<db_port>/<db_name>
$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```