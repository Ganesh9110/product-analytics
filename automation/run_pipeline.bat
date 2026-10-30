@echo off
cd /d E:\Product_Analyst

"C:\Users\kollu\AppData\Local\Programs\Python\Python312\python.exe" -m papermill "E:\Product_Analyst\notebooks\05_Automation_Pipeline.ipynb" "E:\Product_Analyst\reports\05_Automation_Executed.ipynb" --kernel python3 >> "E:\Product_Analyst\automation\logs\scheduled_run.log" 2>&1