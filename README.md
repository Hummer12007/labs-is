## Labs for IS course

Lab 1 (Pacman)
This lab is in the dms, check https://t.me/Mr_Understood for more

Lab 2 (Knowledge base)
Once .exe is launched you will be presented with a console. You can enter commands there, list of commands can be viewed using 'Help' command. 
When entering arguments for commands, you can use " symbol to indicate multiple-word argument.
Here are some useful command examples:
AddData "Test father"
AddData mother
AddData "mother in law"
AddOneWayConnection "Test father" mother wife
AddOneWayConnection mother "mother in law" mother
AddNewRule "All wifes" "Has a wife:" wife
AddNewRule "All Mils" "Has a mil:" wife mother
ApplyRule "Test father" "All wifes"
ApplyRule "Test father" "All Mils"
