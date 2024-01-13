sudo apt-get install git
git version

# first-time config
git config --global user.name "Alfian Hidayatulloh"
git config --global user.email alfianhid@gmail.com
git config --global init.defaultBranch master
git config --global --add safe.directory /home/de-zoomcamp-alfianhid

# ssh setup
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
add pub key to https://github.com/settings/keys

# repo setup
git init
git remote add origin git@github.com:alfianhid/de-zoomcamp-2024.git
git add .
git commit -m "Initial commit"
git push -u origin master