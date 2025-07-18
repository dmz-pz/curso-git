# Para inicializar el contexto de git en un directorio 
# Ejecutamo el comando: git init

# Para empezar a guardar o manejar el control de nuestros primero hay que agregarlos
# Mediante el comando git add <nombre del fichero> 

# Para empezar a tomar la primera foto o lo que vendria siendo el primer cambio para el control de versiones 
# Lo que hacemos es lo que vendria siendo "commit" mediante el comando 'git commit' 

# Para poder volver a un punto de control a una imagen anterior utilizamos el comando git checkout <nombre del fichero>
# en el cual quieres volver a un punto de control anterior donde cabe aclarar permite volver a una imagen o version anterior 

# Cada vez que querememos agregar un nuevo cambio agregamos de nuevo el fichero mediante git add 
# y luego le aplicamos su respectivo commit con el su message del cambio que estamos aplicando

# Tambien podemos controlar como se muestran los logs mediante parametros 
# Si agregamos el parametro --graph nos lo muestra con asteriscos desde el primer commit hasta el ultimo 
# donde manera visual se hace entender mucho mejor a su vez mediante el parametro --pretty=onefile 
# hara que nuestro logs nuestro los commits realizados en una linea resumiendo informacion a el hash 
# y el message que se le añadio. 

# Tambien existen alias que podemos crear y añadirlos a nuestra configuracion global en el cual nos permite 
# ponerles nombres a comandos y asi en vez de escribir el nombre completo del comando completo hacemos llamado
# al nombre asignado en el alias. Para ello ejecutamos el comando: 

# - git config --global alias.<el nombre que le querramos establecer> "Dentro de comillas el comando" 

# Para comparar los cambios que se han realizado en base a los ultimos cambios de una rama usamos el comando 
# git diff esto nos permite ver los cambios que se han realizado en el fichero en base a su utlima imagen  

# Mediante git checkout <hash del commit o imagen a la querramos volver> nos permiter volver a un puntos de control especifico
# Donde hay que tener precaucion ya que si no se han guardado los cambios actualmente puedes perder la informacion

print("Hola git")