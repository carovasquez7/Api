while read line
do 
	wget -P /home/desarrollador/Escritorio/Tutorial/application/quickstart/Descargas $line 

done < ListaUrl.txt