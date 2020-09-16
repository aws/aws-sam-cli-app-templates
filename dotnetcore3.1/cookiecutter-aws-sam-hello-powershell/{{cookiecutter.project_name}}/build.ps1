Import-Module -Name AWSLambdaPSCore

$scriptPath = Join-Path -Path $PSScriptRoot -ChildPath "src/Function.ps1"
$outPath = "artifacts/Function.zip"

# Remove the compiled zip if previously built
if (Test-Path $outPath) {
    Remove-Item -Path $outPath -Force -Confirm:$false
}

New-AWSPowerShellLambdaPackage -ScriptPath $scriptPath -OutputPackage $outPath
