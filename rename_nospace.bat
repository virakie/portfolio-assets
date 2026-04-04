@echo off
setlocal enabledelayedexpansion

set "root=E:\Virak\Portfolio Site\portfolio-assets"

:: Rename files first
for /r "%root%" %%f in (*) do (
    set "name=%%~nxf"
    set "newname=!name: =_!"
    if not "!name!"=="!newname!" (
        ren "%%f" "!newname!"
    )
)

:: Rename folders (deepest first)
for /f "delims=" %%d in ('dir /s /b /ad "%root%" ^| sort /r') do (
    set "name=%%~nxd"
    set "newname=!name: =_!"
    if not "!name!"=="!newname!" (
        ren "%%d" "!newname!"
    )
)

echo Done.
pause