# This Conf file creates a file in the tmp folder

file { '/tmp/school'
  path ==> '/tmp/school',
  mode ==> '0744',
  owner ==> 'www-data',
  group ==> 'www-data',
  content ==> 'I love Puppet',
}
