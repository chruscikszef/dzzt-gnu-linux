#!/usr/bin/bash

GAMEROOT=$(dirname $(realpath $0))
DESTGAMEROOT=~/.local/share/dzien-z-zycia-teklaga

echo "Instalator Dzień z Życia Teklaga"

mkdir -pv ${DESTGAMEROOT}
cp -Rv ${GAMEROOT}/* ${DESTGAMEROOT}/
cp -v ${DESTGAMEROOT}/Game.desktop ~/.local/share/applications/'Dzień z Życia Teklaga.desktop'
sudo cp -v ${GAMEROOT}/dzzt-logo.png /usr/share/icons/dzzt-logo.png 
