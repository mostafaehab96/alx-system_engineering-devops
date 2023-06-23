# Kills a process named killmenow

exec { '/usr/bin/pkill killmenow':
  onlyif => '/usr/bin/pgrep killmenow',
}
