# Changes the upper limit of open files in nginx

exec {"sudo sed -i '/^ULIMIT/s/^ULIMIT.*/ULIMIT=\"n -4096\"/' /etc/default/nginx":
  path  => '/usr/bin',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasstatus  => true,
  hasrestart => true,
}
