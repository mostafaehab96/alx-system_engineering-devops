#Configure ssh_config


$configs = "
Host *
    IdentityFile ~/.ssh/school
	PasswordAuthentication no
"

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $configs,
}
