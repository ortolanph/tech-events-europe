$response = Invoke-RestMethod https://api.chucknorris.io/jokes/random

Write-Host $response.value