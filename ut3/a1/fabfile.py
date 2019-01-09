from fabric.api import env, cd, local, run

# nombre de la máquina de producción
env.hosts = ['cloud']


def deploy():
    local('git push')
    with cd('~/imw/ut3/a1'):
      run('git pull')
    run('supervisorctl restart vmweb')
