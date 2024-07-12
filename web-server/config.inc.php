<?php

// Roundcube configuration
$config = array();

// Database connection string (DSN) for read+write operations
$config['db_dsnw'] = 'mysql://roundcube:password@localhost/roundcubemail';

// SMTP server host
$config['smtp_server'] = 'tls://smtp.example.com';

// SMTP port
$config['smtp_port'] = 587;

// Log sent messages
$config['smtp_log'] = true;

// IMAP host
$config['default_host'] = 'tls://imap.example.com';

// IMAP port
$config['default_port'] = 993;

// Support URL
$config['support_url'] = 'http://support.example.com/';

// Enable plugins
$config['plugins'] = array('archive', 'zipdownload');

// Skin name
$config['skin'] = 'elastic';

?>

