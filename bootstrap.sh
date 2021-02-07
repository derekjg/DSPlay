#!/bin/bash

set -o errexit
set -o pipefail

# Directory to set up venv into.
VENV_DIR="venv"

# Initialize virtualenv subdir.
function init_venv() {
  echo 'Setting up venv...'
  if ! python3 -m venv "${VENV_DIR}"; then
    echo "ERROR: failed to create virtual env dir."
    exit 1
  fi
}

# Installs/updates python packages under venv.
function install_python_requirements() {
  # On buildbot it seems that parallel pip requests can make it fail randomly.
  # If "flock" is present, attempt to use it to prevent multiple parallel
  # bootstrap instances from running.
  echo 'Upgrading...'
  "${VENV_DIR}/bin/pip" install --upgrade pip setuptools wheel virtualenv

  echo 'Installing python packages in venv...'
  "${VENV_DIR}/bin/pip" install --upgrade -e .

  echo 'Installing dev python packages in venv...'
}

cd "$(dirname "$0")"
init_venv
install_python_requirements

echo
echo "Ok!"
echo
