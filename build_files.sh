 echo "BUILD START"
 python3.9 -m pip install --upgrade pip 
 python3.9 -m pip install virtualenv
 virtualenv env
 "env\Scripts\activate"
 python3.9 -m pip install --upgrade setuptools
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"