#This puppet creates a file named school at /tmp directory
# and gives it the following attributes
file { '/tmp/school' :
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love puppet',
}
