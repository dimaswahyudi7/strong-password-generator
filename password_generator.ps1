function Generate-Password {
    $lengthPrefix = 10
    $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    $password = -join ((1..$lengthPrefix) | ForEach-Object { $chars[(Get-Random -Maximum $chars.Length)] })
    $password += 'x' * 6
    return $password
}

Write-Host "Generated Password: $(Generate-Password)"
