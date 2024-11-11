function getUnversionedFileList
{
    [array] $filesToUpdate = git status --short
    return $filesToUpdate
}

function updateRepo
{
    git pull
}

function performGitOps
{
    $currentDate = Get-Date -Format "yyyy-MM-dd - HH:mm"
    git add .
    git commit -m "Commiting update at $currentDate"
    git push
}

updateRepo
python all_countries.py
$unversionedFiles = getUnversionedFileList
$totalUnversionedFiles = $unversionedFiles.Count

if ($totalUnversionedFiles -gt 0) {
    performGitOps
}