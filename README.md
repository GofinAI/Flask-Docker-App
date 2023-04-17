# Flask-Docker-App

Build:
docker build --tag flask-db-test .

Run:
Set environment variables
DBHOST
DBNAME
DBPASSWORD
DBUSER
AWS-ACCOUNT
ECRNAME

docker run  -d -p 5000:5000 -e DBHOST=$DBHOST -e DBUSER=$DBUSER -e DBPASSWORD=$DBPASSWORD -e DBNAME=$DBNAME flask-db-test:latest

Push to ECR:
docker tag flask-db-test $AWS-ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/$ECRNAME
docker push $AWS-ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/custom_docker:flask-db-test
