# fcgiwrap example

## install fcgiwrap
```
apt install fcgiwrap

```

## file permission
### set
```
sudo chown www-data:www-data /run/fcgiwrap.socket
sudo -u www-data /var/www/bashexample/scripts/scls

```

### test
```
sudo -u www-data /var/www/bashexample/scripts/sc-ls
```

## conf for nginx

## script file
need have some meta data such as content-type etc. can NOT be straight up script file.
