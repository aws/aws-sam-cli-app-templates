Import-Module -Name Pester

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$functionPath = Join-Path -Path $here -ChildPath "../src/HelloWorld/Function.ps1" -Resolve

. $functionPath | Out-Null

Describe "HelloWorld Tests" {
    Context "Sample Execution" {

        $mockLocation = "1.2.3.4"

        write-host $result.Body
        It "Should write the input to the host stream" {

            Mock -CommandName "Get-CallingIP" -MockWith {
                return $mockLocation
            }

            $result = Invoke-LambdaHandler

            Assert-MockCalled -CommandName "Get-CallingIP" -Times 1
            (ConvertFrom-Json $result.Body).message | Should -Be "hello world"
            (ConvertFrom-Json $result.Body).location | Should -Be $mockLocation
        }
    }
}
