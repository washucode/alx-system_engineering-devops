# This manifest creates a file in /tmp

file{'school':
    ensure  => file,
    path    => '/tmp/school',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
