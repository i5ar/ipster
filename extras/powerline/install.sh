# Use colors, but only if connected to a terminal, and that terminal
# supports them.
if which tput >/dev/null 2>&1; then
    ncolors=$(tput colors)
fi
if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
  RED="$(tput setaf 1)"
  YELLOW="$(tput setaf 3)"
  BLUE="$(tput setaf 4)"
  NORMAL="$(tput sgr0)"
else
  RED=""
  BLUE=""
  NORMAL=""
fi

# Only enable exit-on-error after the non-critical colorization stuff,
# which may fail on systems lacking tput or terminfo.
set -e

# Get Powerline repository root and copy the configuration files.
# https://stackoverflow.com/questions/12137431/
if [ "$($1 -m pip show powerline-status)" ]; then
  repository_root=$(
    $1 -m pip show powerline-status | grep -oP '(?<=Location: ).*')
  if [ -d "$repository_root" ]; then
    colors_dir="$repository_root/powerline/config_files/colorschemes/ipython/"
    themes_dir="$repository_root/powerline/config_files/themes/ipython/"
    printf "${BLUE}"
    printf "Copying colorscheme file to '$colors_dir' directory.\n"
    cp colorscheme/solarized.json $colors_dir
    printf "Copying theme files to '$themes_dir' directory.\n"
    cp theme/in_agnoster.json $themes_dir
    cp theme/out_agnoster.json $themes_dir
    printf "${NORMAL}"
  fi
else
  printf "${RED}Powerline installation not found for $1!${NORMAL}\n"; exit
fi

# Override Powerline configuration for Terminus.
echo "Configure Powerline? (1/2)"
select font in "No" "Yes"; do
    case $font in
        No)
          break;;
        Yes)
          # Override Powerline configuration for IPython.
          chmod 755 configure.py
          $1 configure.py
          break;;
    esac
done

printf "${BLUE}"
echo ''
echo '    ________       __           '
echo '   /  _/ __ \_____/ /____  _____'
echo '   / // /_/ / ___/ __/ _ \/ ___/'
echo ' _/ // ____(__  ) /_/  __/ /    '
echo '/___/_/   /____/\__/\___/_/     '
echo ''
echo 'Complete!'
printf "${NORMAL}"
