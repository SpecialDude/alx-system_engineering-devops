# Puppet manifest for configuring nginx on a web server


exec { 'Install Nginx':
  command => 'apt-get update && apt-get -y install nginx',
}

exec { 'Create the root folder':
  command => 'mkdir -p /data/www/'
}

file { 'Nginx Config File':
  ensure => present,
  path   => '/etc/nginx/nginx-conf',
}

exec { 'Redirection':
        command => 'sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/nginx-conf'

}


file { 'Nginx Home Page':
  ensure  => present,
  path    => '/data/www/index.html',
  content => 'Hello World!',
}

exec { 'Start Server':
  command => 'systemctl start nginx.service',
}

