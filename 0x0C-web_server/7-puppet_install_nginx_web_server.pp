# Manifest file: 7-puppet_install_nginx_web_server.pp

# Install Nginx

package { 'nginx':
    ensure => "installed",
}

# Define Nginx configuration
file{ '/etc/nginx/sites-available/default':
    content => template('nginx_config/default.erb'),
    notify => Service['nginx']
}

# Create custom HTML files
file { '/var/www/html/index.html':
  content => 'Hello World!',
  notify  => Service['nginx'],
}
file { '/var/www/html/redirect.html':
  content => 'Redirecting...',
  notify  => Service['nginx'],
}

# Default sites
exec { 'enable_default_site':
  command => 'ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
  creates => '/etc/nginx/sites-enabled/default',
  notify  => Service['nginx'],
}

# Redirect

nginx::resource::location { 'redirect_me':
  location => '/redirect_me',
  www_root => '/var/www/html',
  index    => 'redirect.html',
  rewrite  => '^ /redirect_me permanent',
}

# Make sure Nginx is running

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
