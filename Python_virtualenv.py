'''
	Python Tutorial: virtualenv and why you should use virtual environments
	https://www.youtube.com/watch?v=N5vscPTWKOk
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=14

	pip install virtualenv
	mkdir Environments, cd Environments or (cd !$)
	virtualenv {name_of_project}
	
	MAC - source {name_of_project}/bin/activate
	WIN - {name_of_project}\\Scripts\\activate

	where python or where pip

	pip freeze --local > sometextfile.txt

	WIN - rmdir /S {name_of_project}
	MAC - rm -rf {name_of_project}

	virtualenv -p ./Users/Joshua/AppData/Local/Program/Python/{python_version} {name_of_project}

'''

