# Puppet manifest to setup ubuntu server with nginx

exec  {  'update':
  command => 'sudo apt-get update -y',
  path    => '/usr/bin'
}

package  {  'nginx':
  ensure  => installed,
  require => Exec['update']
}

service  {  'nginx':
  ensure => running
}

file  {  '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}

file  {  '/data/web_static':
  ensure => directory
}

file  {  '/data/web_static/releases':
  ensure => directory
}

file  {  '/data/web_static/releases/test':
  ensure => directory
}

file  {  '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Hello Holberton',
}

file  {  '/data/web_static/shared':
  ensure => directory
}

exec  {  'create_link':
  command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  path    => '/usr/bin'
}

exec  {  'update_nginx':
  command => 'sudo sed -i "/server_name _/a\ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-available/default',
  path    => "/usr/bin"
}

exec {  'restart_nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin'
}
