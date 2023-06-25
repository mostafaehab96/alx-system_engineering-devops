#Configure ssh_config


$configs = "
Host ubuntu
    HostName 52.201.157.19
    User ubuntu
    IdentityFile ~/.ssh/school
"

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $configs,
}
