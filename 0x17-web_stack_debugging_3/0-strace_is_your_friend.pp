# Fix error.
exec { 'mod_file':
  command => "/bin/sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php"
}
