@echo off
:: BasicCMD.bat - Comandos básicos para la consola de Windows
:: Fachascript (R) Indentado Version 0.1. Pibe Emoji Studios 2025 Todos los derechos reservados

:: Comando para mostrar la versión de Fachascript
if "%1" == "--Indentado" if "%2" == "--Version" (
    echo Fachascript (R) Indentado Version 0.1. Pibe Emoji Studios 2025 Todos los derechos reservados
    goto :EOF
) 

:menu
echo.
echo ============================
echo  Comandos Básicos de Windows
echo ============================
echo 1. Mostrar fecha y hora
echo 2. Listar archivos en el directorio actual
echo 3. Mostrar la ruta actual
echo 4. Crear un directorio
echo 5. Eliminar un directorio
echo 6. Salir
echo ============================
echo.

set /p choice=Seleccione una opción (1-6): 

if "%choice%" == "1" goto fecha_hora
if "%choice%" == "2" goto listar_archivos
if "%choice%" == "3" goto ruta_actual
if "%choice%" == "4" goto crear_directorio
if "%choice%" == "5" goto eliminar_directorio
if "%choice%" == "6" goto salir

goto menu

:fecha_hora
echo.
echo Fecha y Hora actuales:
date /t
time /t
echo.
pause
goto menu

:listar_archivos
echo.
echo Archivos en el directorio actual:
dir
echo.
pause
goto menu

:ruta_actual
echo.
echo Ruta actual:
cd
echo.
pause
goto menu

:crear_directorio
echo.
set /p dirname=Ingrese el nombre del directorio a crear: 
mkdir "%dirname%"
echo Directorio "%dirname%" creado.
echo.
pause
goto menu

:eliminar_directorio
echo.
set /p dirname=Ingrese el nombre del directorio a eliminar: 
rd /s /q "%dirname%"
echo Directorio "%dirname%" eliminado.
echo.
pause
goto menu

:salir
exit /b

:EOF