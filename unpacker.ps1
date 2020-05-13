$Zipped = "C:\ASX_DATA\ZIPPED"
$Unzipped = "C:\ASX_DATA\UNZIPPED"
$Data = "C:\ASX_DATA\DATA"

Get-ChildItem "$Zipped\*.zip" | % {Expand-Archive $_ -DestinationPath "$Unzipped"} -recurse -Force
Copy-Item -Path "$Unzipped\*\*.txt" -Destination "$Data" -recurse -Force
