@echo off

:::    ____             _                                   _   _____                                    
:::   |  _ \           | |                                 | | |  __ \                                   
:::   | |_) | __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| | | |__) |___ _ __ ___   _____   _____ _ __ 
:::   |  _ < / _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` | |  _  // _ \ '_ ` _ \ / _ \ \ / / _ \ '__|
:::   | |_) | (_| | (__|   < (_| | | | (_) | |_| | | | | (_| | | | \ \  __/ | | | | | (_) \ V /  __/ |   
:::   |____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_| |_|  \_\___|_| |_| |_|\___/ \_/ \___|_|   
:::                          __/ |                                                                       
:::                         |___/                                                                        
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

echo Auto setup...

echo --------------------------[STAGE 1/2]--------------------------
echo create conda environment
call conda env create --file environment.yaml --yes --name background_remover 

echo --------------------------[STAGE 2/2]--------------------------
echo activate environment 
call conda activate background_remover

echo deactivate conda enviromment
call conda deactivate

echo --------------------------DONE--------------------------
pause


