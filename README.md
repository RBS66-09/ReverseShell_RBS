# ReverseShell_RBS
Reverse shell pensada per utilitzar-la amb netcat des de linux.

1.Editar l'arxiu.py i col·locar una IPv4 local(192.168.x.x) i un port(del 0 al 65535) que no estigui ocupat en el moment de l'auditoria. #La ip ha da ser la de la màquina atacant 

<img width="207" height="43" alt="Captura de pantalla 2026-08-20 022846" src="https://github.com/user-attachments/assets/50258bf2-e48d-42d7-8499-ccd6bbe488ce" />


2.Obrir una powershell a una màquina windows i executar la següent ordre: pyinstaller --onefile --noconsole --icon=icon
.ico script.py #Es pot prescindir de tots els paràmetres amb format --paràmetre menys el --onefile, però són 
recomanables<img width="750" height="49" alt="Img01Reverse" src="https://github.com/user-attachments/assets/6c51a55c-725b-41ed-be02-6e0ac1b56515" />

3.Executar la següent ordre a la consola de la màquina atacant: nc -nvlp <<port introduït a l'arxiu.py>><img width="337" height="49" alt="1787186080" src="https://github.com/user-attachments/assets/6ac88ad4-d47e-4fdd-8265-a1b7bc7dbe6f" />

4.Executar l'arxiu.exe i esperar a la connexió

**EL CODI NO ESTÀ OFUSCAT, PER A GARANTIR L'EFECTIVITAT DE L'EINA, CAL OFUSCAR EL CODI O DESACTIVAR L'ANTIVIRUS AL DESCARGAR FINS QUE S'ACABI L'AUDITORIA**
