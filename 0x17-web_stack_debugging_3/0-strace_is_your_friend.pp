# Fixes php issue

exec { 'fix-wordpress':
  command => '/usr/local/bin/:/bin/sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
