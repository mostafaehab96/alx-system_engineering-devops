# Changes the upper limit of open files in nginx

exec {"sudo sed -i 's/-n 15/-n 4096/g' /etc/default/nginx":
  path  => '/usr/bin',
}
