# Changes the user limit for open files

exec {"echo holberton soft nofile 10000 >> /etc/security/limits.conf":
  path => '/bin',
}


exec {"echo holberton hard nofile 20000 >> /etc/security/limits.conf":
  path => '/bin',
}
