# Instamirror
This is a quick python script I made for personal use.

Recommended usage:
- Install dependencies globally:
```bash
sudo pip install savepagenow archiveis
```
- Clone it into your home directory:
```bash
cd ~/
git clone https://github.com/anomiee/instamirror.git
```
- Add the following to your `.bashrc`/`.zshrc`/etc.:
```bash
alias mirror="python ~/instamirror/mirror.py"
```

Now you can mirror any URL at the terminal by doing:
```bash
mirror http://google.com
```
