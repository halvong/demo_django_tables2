Hal Vong
cell: 626.202.6940
halvong@yahoo.com
Dec. 1, 2019

#Commands used for this project
          description                          commands
0. build the image & container:  docker-compose up --build -d
1. starts web and database:      docker-compose up -d
2. login to postgresql database: docker-compose run --rm database psql -U mike -h database
3. creates demo_app:             docker-compose exec web python manage.py startapp demo_app
4.                               docker-compose exec web python manage.py makemigrations demo_app
5.                               docker-compose exec web python manage.py migrate
6. login to container:           docker exec -it <container id> bash
7. run the custom admin command: python manage.py ingest --file demo_data.csv
8. stop containers:              docker-compose stop

