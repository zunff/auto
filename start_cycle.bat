@echo off  
python auto_cycle.py  
if %ERRORLEVEL% neq 0 (  
    echo python 命令执行失败，尝试使用 python3...  
    python3 auto_cycle.py  
    if %ERRORLEVEL% neq 0 (  
        echo python3 命令也执行失败。  
    )  
)
pause