"""

Sublime uses Build systems to determine path for the
python executable & site_packages
C:\\Users\\Joshua\\AppData\\Roaming\\Sublime Text 3\\Packages\\User

CLI commands
	echo %path%

	where python
	
pip list
pip show {any package}
	(observe the path of that package,
	 as it should match sys.executable
	 and/or echo %path% highest python
	 'lib/site_package')

Topic: Virtual Enrivonrments 
	pipenv
"""
import pip
import sys

print(sys.version)
print(sys.executable)

