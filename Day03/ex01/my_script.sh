PYTHON_PATH = "/usr/bin/python3"
DIR = "local_lib"

/usr/local/bin/python3 -m venv local_lib
source local_lib/bin/activate


python3 -m pip --version
python3 -m pip install --upgrade pip
python3 -m pip install --log "pip_install.log" --force-reinstall git+"https://github.com/jaraco/path.git"
python3 my_program.py