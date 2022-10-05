# git-init
A script for git initialization.

## Function

* Check if the git is installed.
* Check if the ssh package is installed.
* Configure the git user name and email.
* Generate the ssh key if it doesn't exist.
* Set the ssh client config to use the ssh key when connecting to github.com.
* Copy the ssh key to the clipboard in order to add it to the github account in webpage.
  
## Usage

1. Download the script.

```bash
$ curl https://raw.githubusercontent.com/hdaojin/git-init/main/git-init.py  > git-init.py
```


2. Run the script.

```bash
$ python3 git-init.py
```

3. Add the ssh public key content to the github account in webpage.
   * The ssh public key content is in the clipboard.
   * Login your github account in webpage.
   * Click the user icon in the top right corner, and then click "Settings" -> "SSH and GPG keys" -> "New SSH key".
   * Write the "Title" and paste the ssh public key content in the "Key" field.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)