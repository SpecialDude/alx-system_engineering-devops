# This script configures a new nginx server

exec {'Update and install nginx':
  command => 'apt-get -y update && apt-get -y install nginx',
  path => '/usr/bin',
}

exec {'Exempt Nginx through firewall':
  command => 'ufw allow \'Nginx HTTP\'',
  path => '/usr/sbin'
}

exec {'Hello Page':
  command => '/usr/bin/echo "Hello World!" > /var/www/html/index.html',
}

exec {'Error Page':
  command => '/usr/bin/echo "Ceci n\'est pas une page" /var/www/html/404.html',
}

exec {'Setup Redirecting':
  command => "/usr/bin/sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
}

exec {'Setup Error page':
  command => '/usr/bin/sed -i \'/listen 80 default_server/a \\\terror_page 404 /404.html;\' /etc/nginx/sites-available/default',
}

exec {'Add custom header':
  command => '/usr/bin/sed -i "/listen 80 default_server/a add_header X-Served-By \'$HOSTNAME\';" /etc/nginx/sites-available/default',
}


exec { 'Restart nginx server':
  command => 'service nginx stop && service nginx start',
  path => ['/usr/sbin', '/usr/bin'],
}
