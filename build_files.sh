echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

echo "MAKE MIGRATIONS"
python3.9 manage.py makemigrations
python3.9 manage.py migrate
echo "END MIGRATIONS"

echo "BUILD END"
