# Installs flask 2.1.0 with pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}