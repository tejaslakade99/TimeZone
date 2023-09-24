echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

echo "MIGRATION STARTED"
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "MIGRATION FINISHED"

winpty python3.9 manage.py createsuperuser --username="Tejas" --email="tejaslakade99@gmail.com"

echo "BUILD END"
