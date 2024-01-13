sudo apt-get install git
git version
git config --global user.name "Alfian Hidayatulloh"
git config --global user.email alfianhid@gmail.com
git config --global init.defaultBranch master
git config --global --add safe.directory /home/de-zoomcamp-alfianhid
git init
git remote add origin git@github.com:alfianhid/de-zoomcamp-2024.git
git add .
git commit -m "Initial commit"
git push -u origin master