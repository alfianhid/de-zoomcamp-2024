```
sudo apt-get install git
```
```
git version
```
# first-time config
```
git config --global user.name "your-name"
```
```
git config --global user.email your-email
```
```
git config --global init.defaultBranch master
```
```
git config --global --add safe.directory /home/your-directory
```
# ssh setup
```
ssh-keygen -t ed25519 -C "your-email"
```
```
eval "$(ssh-agent -s)"
```
```
ssh-add ~/.ssh/your-ssh-private-key-location
```
add your public key to https://github.com/settings/keys
# repo setup
```
git init
```
```
git remote add origin git@github.com:your-username/your-repo-name.git
```
```
git add .
```
```
git commit -m "Initial commit"
```
```
git push -u origin master
```