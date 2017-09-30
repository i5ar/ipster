# Use colors, but only if connected to a terminal, and that terminal
# supports them.
if which tput >/dev/null 2>&1; then
    ncolors=$(tput colors)
fi
if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
  BLUE="$(tput setaf 4)"
  NORMAL="$(tput sgr0)"
else
  BLUE=""
  NORMAL=""
fi

# Only enable exit-on-error after the non-critical colorization stuff,
# which may fail on systems lacking tput or terminfo.
set -e

# Get the username that logged in to the session.
# https://stackoverflow.com/questions/3522341/
CURRENT_USER="$(logname)"
# https://stackoverflow.com/questions/20504662/
CURRENT_HOME=$(eval echo "~$CURRENT_USER")
# Append color options to .tmux.conf file for the current user.
cf="$CURRENT_HOME/.tmux.conf"
if [ -f "$cf" ]; then
  while true; do
    echo "Do you wish to append color configuration to '$cf' file? (y/n)"
    read answer
    case $answer in
      [Yy]*)
          printf "${BLUE}Appending configuration to '$cf' file.${NORMAL}\n"
          echo '' >> $cf
          echo '# Override screen 256 color with true color' >> $cf
          echo 'set-option -ga terminal-overrides ",xterm-256color:Tc"' >> $cf
          break;;
      [Nn]*) break;;
      *) echo "Please answer yes or no.";;
    esac
  done
fi
