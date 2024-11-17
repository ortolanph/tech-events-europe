#!/bin/bash

roundHouseKick() {
    program=$1
    echo "Chuck Norris will not be downloaded 'cause you don't have $program to parse him. You are being Round House Kicked!"
    exit 1
}

checkPartner() {
    program=$1
    check=$(whereis "$program" | awk '{ print $2 }')
    [ -z "$check" ] && roundHouseKick "$program"
}

checkPartner curl
checkPartner jq

result=$(curl -s https://api.chucknorris.io/jokes/random )

echo "$result" | jq -r '.value'