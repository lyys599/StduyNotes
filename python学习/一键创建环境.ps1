$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonLauncher = Get-Command py -ErrorAction SilentlyContinue
if ($pythonLauncher) {
    & py -3.12 -m venv (Join-Path $projectRoot ".venv")
} elseif (Test-Path -LiteralPath "C:\ProgramData\anaconda3\python.exe") {
    & "C:\ProgramData\anaconda3\python.exe" -m venv (Join-Path $projectRoot ".venv")
} else {
    throw "未找到py启动器或C:\ProgramData\anaconda3\python.exe，请在VS Code中先选择Python解释器。"
}
$venvPython = Join-Path $projectRoot ".venv\Scripts\python.exe"
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r (Join-Path $projectRoot "requirements.txt")
& $venvPython (Join-Path $projectRoot "13-VSCode代码\00-环境检查.py")
