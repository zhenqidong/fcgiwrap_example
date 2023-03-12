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
sudo -u www-data /var/www/bashexample/scripts/test
```

## conf for nginx

1. request_body isn't available before it's needed, can be seen when you proxy or cgi_pass
2. document_root is not ending with /
3. SCRIPT_NAME OR SCRIPT_FILENAME needs full path

## script file
need have some meta data such as content-type etc. can NOT be straight up script file.
