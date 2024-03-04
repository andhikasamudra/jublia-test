run: 
	export FLASK_APP=manage.py && flask run

run-debug:
	export FLASK_APP=manage.py && flask run --debug