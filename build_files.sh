echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

echo "MIGRATION STARTED"
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "MIGRATION FINISHED"

echo "BUILD END"
