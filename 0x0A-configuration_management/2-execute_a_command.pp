# This manifest kills a process

exec { 'Kills a Process':
  command => 'pkill -f killmenow',
  path => '/usr/bin/',
}
