# This manifest kills the process killmenow

exec{'pkill':
    command  => 'pkill killmenow',
    provider => 'shell',
}
