- Create your SSH keys locally with a guide in this link: https://cloud.google.com/compute/docs/connect/create-ssh-keys 
- Add your public key to your GCP VM with a guide in this link: https://cloud.google.com/compute/docs/connect/add-ssh-keys 
- Create a `config` file locally with an example below:
```
Host your-hostname
   HostName your-external-ip-address
   User your-username
   IdentityFile ~/.ssh/your-ssh-private-key-location
   UserKnownHostsFile ~/.ssh/your-known-hosts-location
   PasswordAuthentication yes
```
- Install `Remote - SSH` extension on your VSCode with this provided link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh 
- Finally, you can connect to your GCP VM remotely with a guide in this link: https://code.visualstudio.com/docs/remote/ssh or https://code.visualstudio.com/docs/remote/ssh-tutorial