# SysIMiBio
Sistema de gestión de datos ecológicos y de biodiversidad del [IMiBio](www.imibio.misiones.gob.ar)

## como desarrollar
1. Haga un Clone del repositorio
1. Crea un ambiente virtual env (python)
1. Active el ambiente virtual env
1. Haga la instalación de las dependencias
1. Configure la instancia com .env
1. Ejecute los testes

```console
git clone git@github.com:FelipeSBarros/sysimibio.git sysimibio
cd sysimibio
python -m venv .sysimibio
source .sysimibio/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-semple .env
python manage test 
```

## Deploy en Heroku

1. crie una instancia en [heroku](www.heroku.com)
1. envie las configuraciones para heroku
1. defina secretkey para la instancia
1. cambie DEBUG=False

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`ýthon contrib/secret_gen.py`
heroku config:set DEBUG=False
gut push heroku master --force
```

## Proceso de desarrollo

Más al respecto del [proceso de desarrolo](./Creation_process.md)