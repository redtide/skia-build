#!/bin/bash
set -o errexit -o nounset -o pipefail
setup() {
  local packages=(
    curl
    fontconfig
    libfontconfig1-dev
    libglu1-mesa-dev
    ninja-build
    zip
  )
  sudo apt-get update && sudo apt-get install ${packages[@]}
}
setup
