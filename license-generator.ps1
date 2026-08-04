param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("validate", "generate")]
    [string]$Command,

    [Parameter(Mandatory = $true, Position = 1)]
    [string]$Profile,

    [Parameter(Mandatory = $false)]
    [string]$Out,

    [switch]$Json
)

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$generator = Join-Path $projectRoot "src\license_generator.py"
$pythonArgs = @()
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
$pythonExecutable = $null

if ($pythonCommand) {
    $pythonExecutable = $pythonCommand.Source
}
else {
    $pythonCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        $pythonExecutable = $pythonCommand.Source
        $pythonArgs += "-3"
    }
}

if (-not $pythonExecutable) {
    $bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    if (Test-Path -LiteralPath $bundledPython) {
        $pythonExecutable = $bundledPython
    }
}

if (-not $pythonExecutable) {
    throw "Python 3.11 or later was not found. Install Python or provide it on PATH."
}

$arguments = @($pythonArgs) + @($generator, $Command, $Profile)
if ($Command -eq "generate") {
    if (-not $Out) {
        throw "-Out is required for the generate command."
    }
    $arguments += @("--out", $Out)
}
elseif ($Json) {
    $arguments += "--json"
}

& $pythonExecutable @arguments
exit $LASTEXITCODE
