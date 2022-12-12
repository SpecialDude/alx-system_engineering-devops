# Makes an ssh configuration file

file { 'ssh configuration':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
}

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentitiesOnly yes',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
