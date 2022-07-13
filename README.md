# Machine_Leaning_project
this is my first machine learning project


# conda enviroment :
seprate enviroment fot the project

conda create -p venv python==3.7 -y
# -p will  create the new enviroment in the filder itself it should be preferd
# -n will create the new enviroment in c drive
conda activate venv/

gitignore : the folder in which we place the folder which we dont dont to maintain by git . if we dont want to place the venv folder in git we can place it in the gitignore.

if we want to maintain the version of a file then we need to add it on git using command git command file1 file2  filen
and to add all the file git add .

git status:
if you create a file and it is not added to the git then git status will show the status of file as a warning. 

git log:
to see all the previous versions of your project maintain by git.

to commit:
to create version / commit all changes by git
git commit -m "message:"

to send version /changes to github
git push origin main

To check remote url 
git remote -v

to set up CI/CD pipeline in heroku we need 3 information:


Heroku email:hjain4605@gmail.com
Heroku API_KEY:dac9b876-ef69-4c59-9352-e7aec82d19c4
Heroku_APP_NAME:ml-regression-model1

for deployment we create Dockerfile:

Then build Image:
docker buld -t<image_name>:<tagname>.
# Image name for docker must be lowercase

To list docker image
command : docker images

To run the docker image:
docker run -p 5000:5000 -e PORT=5000 IMAGIE_ID

TO check the running conatainers :
docker ps

To stop any docker container:
docker stop container_ID


