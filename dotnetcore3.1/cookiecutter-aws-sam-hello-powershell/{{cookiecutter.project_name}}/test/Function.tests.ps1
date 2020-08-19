Import-Module -Name Pester

$srcRoot = Join-Path -Path $PSScriptRoot -ChildPath "../src" -Resolve
.$srcRoot\Function.ps1

Describe "HelloWorld Tests" {

    Mock -CommandName "Write-Host" -MockWith { }

    It "Should return a normal crafted return when the function is executed normally" {
        $eval = Write-HelloWorld
        $eval.message | Should BeExactly "hello world"
    }
    It "Should return a a properly formed API return when an API call is made." {
        $LambdaInput = @{
            requestContext = @{
                apiId = '1234567890'
            }
        }
        $eval = Write-HelloWorld
        $eval.statusCode | Should BeExactly 200
        ($eval.body | ConvertFrom-Json).message | Should BeExactly "hello world"
    }
}
