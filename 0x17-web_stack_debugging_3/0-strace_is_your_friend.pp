#Fixes the apache 500 web server errro

exec {"sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php":
  path  => '/usr/bin',
}
