@echo off
for %%f in (*.*) do (
    set "fname=%%~nf"
    set "ext=%%~xf"
    setlocal enabledelayedexpansion
    set "newname=!fname:compressO-=!"
    ren "%%f" "!newname!_compressed!ext!"
    endlocal
)