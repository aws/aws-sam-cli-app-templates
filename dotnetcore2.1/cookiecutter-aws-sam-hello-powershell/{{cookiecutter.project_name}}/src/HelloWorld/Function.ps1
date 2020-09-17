# PowerShell script file to be executed as a AWS Lambda function. 
# 
# When executing in Lambda the following variables will be predefined.
#   $LambdaInput - A PSObject that contains the Lambda function input data.
#   $LambdaContext - An Amazon.Lambda.Core.ILambdaContext object that contains information about the currently running Lambda environment.
#
# The last item in the PowerShell pipeline will be returned as the result of the Lambda function.
#
# To include PowerShell modules with your Lambda function, like the AWSPowerShell.NetCore module, add a "#Requires" statement 
# indicating the module and version.

#Requires -Modules @{ModuleName='AWS.Tools.Common';ModuleVersion='4.1.0.0'}

# This line publishes the input to CloudWatch logs so you know what triggered the function
Write-Host (ConvertTo-Json -InputObject $LambdaInput -Compress -Depth 5)

function Get-CallingIP {
    [CmdletBinding()]
    param()

    $result = Invoke-WebRequest -Uri "http://checkip.amazonaws.com/" `
                                -UserAgent "AWS Lambda PowerShell Client" 
    return [System.Text.Encoding]::ASCII.GetString($result.Content).Replace([environment]::NewLine, $null)
}

function Invoke-LambdaHandler {
    [CmdletBinding()]
    param(
        $LambdaInput,
        $LambdaContext
    )

    $location = Get-CallingIP
    $body = @{
        "message" = "hello world"
        "location" = $location
    }
    
    return @{
        "Body" = ConvertTo-Json -InputObject $body -Compress
        "StatusCode" = 200
        "Headers" = @{
            "Content-Type" = "application/json"
        }
    }
}

return Invoke-LambdaHandler($LambdaInput, $LambdaContext)
