import os, sys, argparse, contextlib, django, csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from core.settings import DATABASES
from ports.models import Port

def resetDatabase():
	# Remove database file if exists
	with contextlib.suppress(FileNotFoundError):
		os.remove(DATABASES['default']['NAME'])

	# Remove migrations
	os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
	os.system('find . -path "*/migrations/*.pyc" -delete')

	# Rebuild database
	os.system('python3 manage.py makemigrations')
	os.system('python3 manage.py migrate')

def createPort(name, port, protocol, description):
	try:
		port = int(port)
		port = Port(name=name, port=port, protocol=protocol, description=description)
		port.save()
	except ValueError:
		# TODO: There is a large number of these at the end of the list
		print("Cannot convert port to Int")
		# input("Holding for value error..")
		pass

def setports():
	with open('../service-names-port-numbers.csv', newline='') as csvfile:
		portmapper = csv.reader(csvfile, delimiter=',')
		next(portmapper)
		for row in portmapper:
			print(row[0], row[1], row[2], row[3])
			if "-" in row[1]:
				portrange = row[1].split('-')
				start = int(portrange[0])
				end   = int(portrange[1])
				print(start, end)
				for x in range(start, end):
					createPort(row[0], x, row[2], row[3])
			else:
				createPort(row[0], row[1], row[2], row[3])


def main():
	resetDatabase()
	setports()

if __name__ == "__main__":
	main()