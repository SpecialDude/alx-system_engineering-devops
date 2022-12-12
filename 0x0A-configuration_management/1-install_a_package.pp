# Installing Packages

exec { 'Flask Installation':
  command => 'pip3 install flask==2.1.0'
}
